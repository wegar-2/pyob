from dataclasses import dataclass, field

from pyob.order.limit_order import LimitOrder


@dataclass
class IcebergOrder(LimitOrder):
    peak: int | None = None
    visible: int = field(init=False)

    def __post_init__(self):
        super(IcebergOrder, self).__post_init__()

        if self.peak is None:
            self.peak = self.quantity

        if self.peak <= 0:
            raise ValueError(f"Invalid peak of iceberg: {self.peak:_}")

        self.visible = min(self.peak, self.quantity)

    def _replenish(self):
        """Placeholder for handling cases when all visible gets exhausted"""
        pass

    def fill(self, quantity: int):
        super(IcebergOrder, self).fill(quantity)
        # not fully implemented yet
        self.visible -= quantity
