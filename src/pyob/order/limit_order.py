from dataclasses import dataclass, field
from pyob.order.order import Order


@dataclass(slots=True)
class LimitOrder(Order):
    remaining: int = field(init=False, repr=True)

    def __post_init__(self):
        super(LimitOrder, self).__post_init__()
        self.remaining = self.quantity

    def fill(self, quantity: int):
        if quantity <= 0:
            raise ValueError(f"Invalid fill quantity: {quantity:_}")
        if quantity > self.remaining:
            raise ValueError(f"Trying to fille {quantity:_} which is more "
                             f"that remaining {self.remaining:_}")
        self.remaining -= quantity
