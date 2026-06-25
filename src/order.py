from dataclasses import dataclass
from side import Side

__all__ = ["Order"]


@dataclass
class Order:
    order_id: int
    side: Side
    quantity: int
    price: int
