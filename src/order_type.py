from enum import Enum

__all__ = ["OrderType"]


class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
