from pyob.order.order import Order


class LimitOrder(Order):
    remaining: int

    def __post_init__(self):
        pass

    def fill(self, quantity: int):
        pass
