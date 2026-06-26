from bisect import insort
from collections import deque

from side import Side
from order import Order


__all__ = ["BookSide"]


class BookSide:

    def __init__(self, side: Side):
        self.side = side
        self.prices = []
        self.levels: dict[int, deque[Order]] = {}
        self.orders: dict[int, tuple[int, Order]] = {}

    def add_order(self, order: Order) -> None:

        if order.price not in self.levels:
            self.levels[order.price] = deque()
            insort(self.prices, order.price)

        self.levels[order.price].append(order)
        self.orders[order.order_id] = (order.price, order)

    def best_price(self) -> int | None:

        if len(self.prices) == 0:
            return None

        if self.side == Side.BUY:
            return self.prices[-1]
        return self.prices[0]

    def best_order(self) -> Order | None:
        best_price = self.best_price()
        if best_price is None:
            return None
        else:

            dq = self.levels[best_price]

            while dq[0].quantity > 0 and len(dq) > 0:
                dq.popleft()

            return dq[0]

    def clear_empty_orders_at_best_price(self):

        best_price = self.best_price()

        if best_price is None:
            return None

        dq = self.levels[best_price]

        while dq[0].quantity == 0 and len(dq) > 0:
            popped = dq.popleft()
            self.orders.pop(popped.order_id, None)

    def cancel(self, order_id: int) -> bool:

        if order_id not in self.orders:
            return False

        # lazy removal
        _, order = self.orders.pop(order_id)
        order.quantity = 0
        return True

