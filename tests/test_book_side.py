from pyob.clob.book_side import BookSide
from pyob.common.side import Side
from pyob.order.limit_order import LimitOrder

from pytest import raises, fixture


def test_book_side_invalid_side():
    with raises(TypeError):
        BookSide(123)


def test_book_side_len():
    book_side = BookSide(Side.BUY)
    assert not book_side
    book_side.add(LimitOrder(Side.BUY, 10, 100))
    assert book_side


def test_cannot_add_empty_limit_order():
    pass


# def test_cannot_add_empty_iceberg():
#     pass
#
#
# def test_best_methods_buy_side():
#     pass
#
#
# def test_best_methods_sell_side():
#     pass
