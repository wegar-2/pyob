from dataclasses import dataclass, field

from pyob.order.limit_order import LimitOrder


@dataclass
class IcebergOrder(LimitOrder):
    peak: int | None = None
    visible: int = field(init=False)

    @property
    def displayed(self):
        return self.visible

    def __post_init__(self):
        super(IcebergOrder, self).__post_init__()

        if self.peak is None:
            self.peak = self.quantity

        if self.peak <= 0:
            raise ValueError(f"Invalid peak of iceberg: {self.peak:_}")

        self.visible = min(self.peak, self.quantity)

    def replenish(self) -> bool:
        """Placeholder for handling cases when all visible gets exhausted"""
        if self.visible > 0 or self.remaining == 0:
            return False
        self.visible = min(self.peak, self.remaining)
        return True

    def fill(self, quantity: int):
        super(IcebergOrder, self).fill(quantity)
        # not fully implemented yet
        if quantity > self.visible:
            raise NotImplemented(f"Hasn't implemented replenishment yet!")
        self.visible -= quantity
