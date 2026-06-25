from dataclasses import dataclass

__all__ = ["Trade"]


@dataclass
class Trade:
    aggressor_order_id: int
    resting_order_id: int
    quantity: int
    price: int
