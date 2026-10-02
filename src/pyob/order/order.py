from dataclasses import dataclass, field

from pyob.common.side import Side


@dataclass(slots=True)
class Order:
    order_id: int = field(init=False, repr=True)
    side: Side
    quantity: int
    price: int

    _orders_counter: int = 0

    def _next_order_id(self) -> int:
        self._orders_counter += 1
        return self._orders_counter

    def __post_init__(self):
        self.order_id = self._next_order_id()

        if self.quantity <= 0:
            raise ValueError(f"Supplied invalid quantity: {self.quantity:_}")

        if not isinstance(self.side, Side):
            raise TypeError(f"Supplied invalid side - not instance of "
                            f"{Side.__name__}")
