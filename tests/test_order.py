from pyob.order.order import Order
from pyob.common.side import Side

from pytest import raises


def test_order_invalid_quantity():
    with raises(ValueError):
        Order(Side.BUY, quantity=0, price=100)
    with raises(ValueError):
        Order(Side.BUY, quantity=-1, price=100)


def test_order_invalid_quantity_type():
    with raises(TypeError):
        Order(Side.SELL, 123.44, 100)


def test_order_invalid_price_type():
    with raises(TypeError):
        Order(Side.SELL, 10, 99.5)


def test_order_invalid_side():
    with raises(TypeError):
        Order(
            "asdf", # noqa
            quantity=1,
            price=100
        )

def test_order_valid():
    assert isinstance(
        Order(Side.BUY, quantity=10, price=100),
        Order
    )
