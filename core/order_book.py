import heapq
from collections import deque
import pandas as pd
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


    def remove_order(self, order_id: int, side: str):
        book = self.bids if side == "buy" else self.asks
        for price in book:
            orders = book[price]
            for i, order in enumerate(orders):
                if order.order_id == order_id:
                    orders.remove(order)
                    if not orders:
                        del book[price]
                    return True
        return False

    def match_order(self):
        trades = []

        bid_prices = sorted(self.bids.keys(), reverse=True)
        ask_prices = sorted(self.asks.keys())

        while bid_prices and ask_prices and bid_prices[0] >= ask_prices[0]:
            best_bid = bid_prices[0]
            best_ask = ask_prices[0]

            bid_orders = self.bids[best_bid]
            ask_orders = self.asks[best_ask]

            while bid_orders and ask_orders and bid_orders[0].quantity > 0 and ask_orders[0].quantity > 0:
                bid_order = bid_orders[0]
                ask_order = ask_orders[0]

                trade_quantity = min(bid_order.quantity, ask_order.quantity)
                trade_price = (best_bid + best_ask) / 2

                trades.append((bid_order.order_id, ask_order.order_id, trade_price, trade_quantity))

                bid_order.quantity -= trade_quantity
                ask_order.quantity -= trade_quantity

                if bid_order.quantity == 0:
                    bid_orders.popleft()
                if ask_order.quantity == 0:
                    ask_orders.popleft()

            if not bid_orders:
                del self.bids[best_bid]
                bid_prices.pop(0)
            if not ask_orders:
                del self.asks[best_ask]
                ask_prices.pop(0)

            trades = pd.DataFrame(trades, columns=['bid_order_id', 'ask_order_id', 'price', 'quantity'])
