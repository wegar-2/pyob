from dataclasses import dataclass
from order_type import OrderType
from side import Side
from itertools import count

__all__ = ["Order"]

_order_ids = count(1)


@dataclass
class Order:
    side: Side
    quantity: int
    order_type: OrderType
    price: float | None = None
    order_id: int | None = None

    def __post_init__(self):

        if self.order_id is None:
            self.order_id = next(_order_ids)

        if self.quantity <= 0:
            raise ValueError("Order quantity has to be positive")

        if self.order_type == OrderType.LIMIT and self.price is None:
            raise ValueError("LIMIT order has to have price! ")

        if self.order_type == OrderType.MARKET and self.price is not None:
            raise ValueError("MARKET order cannot have price assigned")
