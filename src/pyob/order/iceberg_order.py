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

        if (t := type(self.peak)) is not int:
            raise TypeError(f"Iceberg's peak is not an int, it's {t} instead")

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

        if (t := type(quantity)) is not int:
            raise TypeError(f"Invalid type of quantity to be filled: {t}")

        if quantity > self.visible:
            raise ValueError(f"Quantity to fill: {quantity:_} exceeds the "
                             f"visible quantity {self.visible:_}")

        super(IcebergOrder, self).fill(quantity)
        self.visible -= quantity
