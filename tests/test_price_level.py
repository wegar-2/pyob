from pyob.clob.price_level import PriceLevel
from pyob.order.limit_order import LimitOrder
from pyob.common.side import Side

from pytest import fixture, raises


@fixture
def limos() -> list[LimitOrder]:
    return [
        LimitOrder(Side.BUY, 10, 100),
        LimitOrder(Side.BUY, 8, 100),
        LimitOrder(Side.BUY, 15, 100),
    ]


@fixture
def price_level(limos) -> PriceLevel:
    pl = PriceLevel(Side.BUY, 100)
    for limo in limos:
        pl.add(limo)
    return pl


def test_price_level_invalid_order_price():
    pl = PriceLevel(Side.BUY, 100)
    with raises(ValueError):
        pl.add(LimitOrder(Side.BUY, 10, 99))


def test_price_level_invalid_order_side():
    pl = PriceLevel(Side.BUY, 100)
    with raises(ValueError):
        pl.add(LimitOrder(Side.SELL, 10, 100))


def test_price_level_order_doubled():
    pl = PriceLevel(Side.BUY, 100)
    limo = LimitOrder(Side.BUY, 10, 100)
    pl.add(limo)
    with raises(ValueError):
        pl.add(limo)


def test_price_level_first(limos, price_level):
    assert limos[0] is price_level.first()


def test_price_level_remove(limos, price_level):
    price_level.remove(limos[0].order_id)
    assert price_level.first() is limos[1]