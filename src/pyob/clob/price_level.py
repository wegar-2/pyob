from collections import OrderedDict

from pyob.order.limit_order import LimitOrder
from pyob.common.side import Side


class PriceLevel:

    def __init__(self, side: Side, price: int):
        self.side = side
        self.price = price
        self._orders: OrderedDict[int, LimitOrder] = OrderedDict()

    def add(self, order: LimitOrder):
        if (os := order.side) != self.side:
            raise ValueError(
                f"Order's side {os} is inconsistent with this level's "
                f"side {self.side}")

        if (op := order.price) != self.price:
            raise ValueError(
                f"Inconcistent prices: order's is {op}, "
                f"level's is {self.price}")

        if (oid := order.order_id) in self._orders:
            raise ValueError(f"Order with ID {oid} is already present "
                             f"at this price level! ")

        if order.displayed <= 0:
            raise ValueError(
                f"Cannot add order with non-positive displayed quantity!")

        self._orders[order.order_id] = order

    def __len__(self) -> int:
        return len(self._orders)

    def first(self) -> None | LimitOrder:
        return next(iter(self._orders.values()), None)

    def remove(self, order_id: int) -> None | LimitOrder:
        return self._orders.pop(order_id, None)

    def move_to_back(self, order_id: int) -> None:
        self._orders.move_to_end(order_id)
