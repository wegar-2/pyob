from book_side import BookSide
from side import Side
from trade import Trade
from order import Order


class OrderBook:

    def __init__(self):
        self.bids = BookSide(Side.BUY)
        self.asks = BookSide(Side.SELL)

    def match(self, order: Order) -> list[Trade]:

        if order.side == Side.BUY:
            own_side = self.bids
            opposite_side = self.asks
        else:
            own_side = self.asks
            opposite_side = self.bids

        trades: list[Trade] = []

        # matching logic

        if order.quantity > 0:
            own_side.add_order(order)

        return trades
