from dataclasses import dataclass


@dataclass
class Trade:
    aggressor_order_id: int
    resting_order_id: int
    quantity: int
    price: int
