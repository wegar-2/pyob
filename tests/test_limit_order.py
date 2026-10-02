from pyob.order.limit_order import LimitOrder
from pyob.common.side import Side

from pytest import raises, fixture

@fixture
def limo() -> LimitOrder:
    return LimitOrder(Side.BUY, 10, 100)


def test_limit_order_zero_quantity():
    with raises(ValueError):
        LimitOrder(side=Side.BUY, quantity=0, price=10)


def test_limit_order_negative_quantity():
    with raises(ValueError):
        LimitOrder(side=Side.BUY, quantity=-10, price=10)


def test_limit_order_valid_order():
    assert isinstance(
        LimitOrder(
            Side.BUY,
            quantity=10,
            price=100
        ),
        LimitOrder
    )


def test_limit_order_zero_fill_quantity(limo):
    with raises(ValueError):
        limo.fill(0)


def test_limit_order_negative_fill_quantity(limo):
    with raises(ValueError):
        limo.fill(-200)


def test_limit_order_too_high_fill(limo):
    with raises(ValueError):
        limo.fill(11)


def test_limit_order_valid_quantity(limo):
    limo.fill(5)
    assert limo.remaining == 5
