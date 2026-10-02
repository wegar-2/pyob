from dataclasses import dataclass, field
from itertools import count
from typing import ClassVar, Iterator

from pyob.common.side import Side


@dataclass(slots=True)
class Order:
    order_id: int = field(init=False, repr=True)
    side: Side
    quantity: int
    price: int

    _orders_counter: ClassVar[Iterator[int]] = count(1)

    def __post_init__(self):
        self.order_id = next(Order._orders_counter)

        if self.quantity <= 0:
            raise ValueError(f"Supplied invalid quantity: {self.quantity:_}")

        if t := type(self.quantity) is not int:
            raise TypeError(f"Invalid type of quantity parameter: {t}")

        if t := type(self.price) is not int:
            raise TypeError(f"Invalid type of price parameter: {t}")

        if type(self.side) is not Side:
            raise TypeError(f"Supplied invalid side - not instance of "
                            f"{Side.__name__}")
