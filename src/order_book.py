from src.book_side import BookSide
from src.side import Side
from src.trade import Trade
from src.order import Order

__all__ = ["OrderBook"]


class OrderBook:

    def __init__(self):
        self.bids = BookSide(Side.BUY)
        self.asks = BookSide(Side.SELL)

    @staticmethod
    def _check_if_crosses(
            order: Order,
            opposite_side: BookSide
    ) -> bool:
        if opposite_side.best_price() is None:
            return False
        if order.side == Side.BUY:
            if opposite_side.best_price() <= order.price:
                return True
            return False
        if opposite_side.best_price() >= order.price:
            return True
        return False

    def submit(self, order: Order) -> list[Trade]:

        if order.side == Side.BUY:
            own_side = self.bids
            opposite_side = self.asks
        else:
            own_side = self.asks
            opposite_side = self.bids

        trades: list[Trade] = []

        while order.quantity > 0 and self._check_if_crosses(order, opposite_side):

            if opposite_side.best_price() is None:
                break
            best_order = opposite_side.best_order()

            traded_quantity = min(best_order.quantity, order.quantity)

            trade = Trade(
                aggressor_order_id=order.order_id,
                resting_order_id=best_order.order_id,
                quantity=traded_quantity,
                price=best_order.price
            )

            trades.append(Trade(
                aggressor_order_id=order.order_id,
                resting_order_id=best_order.order_id,
                quantity=traded_quantity,
                price=best_order.price
            ))

            order.quantity -= trade.quantity
            best_order.quantity -= trade.quantity

            opposite_side.clear_empty_orders_at_best_price()

        if order.quantity > 0:
            own_side.add_order(order)

        return trades
