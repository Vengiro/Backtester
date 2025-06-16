import yfinance as yf
import matplotlib.pyplot as plt
from core.strategy import Strategy
from core.display import plot_data
from core.data_feed import DataFeed
from core.data_loader import DataLoader
from core.portfolio import Portfolio

class Backtester:
    def __init__(self, strategy: Strategy, data_loader: DataLoader, portfolio: Portfolio):
        """
        Initialize the Backtester with a strategy, data loader, and portfolio.

        :param strategy: Strategy to be tested.
        :param data_loader: DataLoader to load historical data.
        :param portfolio: Portfolio to manage trades and cash.
        """
        self.strategy = strategy
        self.data_loader = data_loader
        self.portfolio = portfolio
        self.data_feed = DataFeed(self.data_loader.load())



    def run(self):
        """
        Run the backtesting process.
        This method will iterate through the data, generate signals, and execute trades.
        """
        while self.data_feed.has_next():
            data_point = self.data_feed.next()
            self.strategy.update_history(data_point)
            orders = self.strategy.generate_order()

            for order in orders:
                self.portfolio.execute(order, data_point['Close'])