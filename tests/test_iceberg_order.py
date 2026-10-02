from pyob.order.iceberg_order import IcebergOrder
from pyob.common.side import Side

from pytest import raises, fixture


@fixture
def ibo() -> IcebergOrder:
    return IcebergOrder(side=Side.BUY, quantity=10, price=100, peak=5)


def test_ib_order_zero_peak():
    with raises(ValueError):
        IcebergOrder(
            Side.BUY,
            quantity=10,
            price=100,
            peak=0
        )


def test_ib_order_negative_peak():
    with raises(ValueError):
        IcebergOrder(
            Side.BUY,
            quantity=10,
            price=100,
            peak=-10
        )


def test_ib_order_negative_peak():
    ibo = IcebergOrder(Side.BUY, quantity=10, price=100, peak=5)
    assert isinstance(ibo, IcebergOrder)


def test_ib_order_negative_peak():
    ibo = IcebergOrder(Side.BUY, quantity=10, price=100, peak=5)
    assert isinstance(ibo, IcebergOrder)


def test_ib_order_fill(ibo):
    ibo.fill(3)
    assert ibo.remaining == 7
    assert ibo.visible == (5 - 3)
    assert ibo.quantity == 10
