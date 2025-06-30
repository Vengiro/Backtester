import heapq
from collections import deque

class Order:
    def __init__(self, order_id, price, quantity, side, timestamp):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.side = side
        self.timestamp = timestamp

class LimitOrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}

    def add_order(self, order: Order):
        book = self.bids if order.side == "buy" else self.asks
        if order.price not in book:
            book[order.price] = deque()
        book[order.price].append(order)