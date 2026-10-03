from sortedcontainers import SortedDict

from pyob.common.side import Side
from pyob.order import LimitOrder
from pyob.clob.price_level import PriceLevel


class BookSide:

    def __init__(self, side: Side):
        if (t := type(side)) is not Side:
            raise TypeError(f"Invalid type of side argument: {t}")
        self.side = side
        self._price_levels: SortedDict[int, PriceLevel] = SortedDict()

    def __len__(self) -> int:
        return len(self._price_levels)

    def add(self, order: LimitOrder) -> None:

        if (os := order.side) != self.side:
            raise ValueError(f"Inconsistent side of book: {self.side} "
                             f"and order: {os}")

        if order.price in self._price_levels:
            self._price_levels[order.price].add(order)
        else:
            self._price_levels[order.price] = order

    def best_level(self) -> PriceLevel:
        return (
            self._price_levels[-1]
            if self.side == Side.BUY
            else self._price_levels[0]
        )

    def best_price(self) -> int:
        return self.best_level().price

    def best_order(self) -> LimitOrder:
        return self.best_level().first()
