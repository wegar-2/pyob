from src import Order, OrderBook, Side


if __name__ == "__main__":

    o1_buy = Order(
        order_id=1,
        side=Side.BUY,
        quantity=10,
        price=100
    )

    o2_sell = Order(
        order_id=2,
        side=Side.SELL,
        quantity=20,
        price=105
    )

    ob = OrderBook()

    ob.submit(o1_buy)
    ob.submit(o2_sell)

    trades = ob.submit(Order(
        order_id=3,
        side=Side.BUY,
        price=110,
        quantity=5
    ))

    ob.bids.best_order()
    ob.asks.best_order()

    print("halt! ")
