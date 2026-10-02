from pyob.common.side import Side
from pyob.order.order import Order
from pyob.order.limit_order import LimitOrder
from pyob.order.iceberg_order import IcebergOrder


def test_orders_ids():

    orders = [
        Order(Side.BUY, 10, 100),
        LimitOrder(Side.BUY, 10, 100),
        IcebergOrder(Side.BUY, 10, 100, 5)
    ]

    order_ids = [o.order_id for o in orders]

    assert all(oid > 0 for oid in order_ids)
    assert len(set(order_ids)) == len(order_ids)
