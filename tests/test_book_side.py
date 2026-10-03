from pyob.clob.book_side import BookSide
from pyob.common.side import Side
from pyob.order.limit_order import LimitOrder

from pytest import raises, fixture


@fixture
def buy_limos() -> list[LimitOrder]:
    return [
        LimitOrder(Side.BUY, 10, 100),
        LimitOrder(Side.BUY, 10, 101),
        LimitOrder(Side.BUY, 10, 102)
    ]


@fixture
def sell_limos() -> list[LimitOrder]:
    return [
        LimitOrder(Side.SELL, 10, 100),
        LimitOrder(Side.SELL, 10, 101),
        LimitOrder(Side.SELL, 10, 102)
    ]


def test_book_side_invalid_side():
    with raises(TypeError):
        BookSide(123)


def test_book_side_len():
    book_side = BookSide(Side.BUY)
    assert not book_side
    book_side.add(LimitOrder(Side.BUY, 10, 100))
    assert book_side


def test_cannot_add_empty_limit_order():
    book_side = BookSide(Side.BUY)
    limo = LimitOrder(Side.BUY, 5, 10)
    limo.fill(5)
    assert limo.remaining == 0
    with raises(ValueError):
        book_side.add(limo)


def test_best_methods_buy_side(buy_limos):
    book_side = BookSide(Side.BUY)
    for limo in buy_limos:
        book_side.add(limo)
    assert book_side.best_price() == 102
    assert book_side.best_order() == buy_limos[-1]


def test_best_methods_sell_side(sell_limos):
    book_side = BookSide(Side.SELL)
    for limo in sell_limos:
        book_side.add(limo)
    assert book_side.best_price() == 100
    assert book_side.best_order() == sell_limos[0]
