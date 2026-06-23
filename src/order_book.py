from collections import defaultdict, deque
import heapq

from order import Order


class OrderBook:

    def __init__(self):

        # self.bids, self.asks --- both map price to dicts
        self.bids: defaultdict[float, deque[Order]] = defaultdict(deque)
        self.asks: defaultdict[float, deque[Order]] = defaultdict(deque)

        self.orders: dict[int, Order] = {}

