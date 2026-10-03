from sortedcontainers import SortedDict

from pyob.common.side import Side
from pyob.order.limit_order import LimitOrder
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
            new_price_level = PriceLevel(order.side, order.price)
            new_price_level.add(order)
            self._price_levels[order.price] = new_price_level

    def best_level(self) -> PriceLevel | None:
        if not self._price_levels:
            return None
        idx = -1 if self.side == Side.BUY else 0
        return self._price_levels.peekitem(idx)[1]

    def best_price(self) -> int | None:
        bl = self.best_level()
        return None if bl is None else bl.price

    def best_order(self) -> LimitOrder | None:
        bl = self.best_level()
        return None if bl is None else bl.first()
