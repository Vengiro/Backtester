import yfinance as yf
import matplotlib.pyplot as plt
from core.strategy import Strategy
from core.display import plot_data
from core.data_feed import DataFeed
from core.data_loader import DataLoader
from core.portfolio import PortfolioManager

map = { "buy": 1, "sell": -1, "hold": 0 }


class Backtester:
    def __init__(self, strategy: Strategy, data_loader: DataLoader, portfolioManager: PortfolioManager, ticker: str):
        """
        Initialize the Backtester with a strategy, data loader, and portfolio.

        :param strategy: Strategy to be tested.
        :param data_loader: DataLoader to load historical data.
        :param portfolio: Portfolio to manage trades and cash.
        """
        self.strategy = strategy
        self.data_loader = data_loader
        self.portfolioManager = portfolioManager
        self.data_feed = DataFeed(self.data_loader.load())
        self.ticker = ticker
        self.history = []



    def run(self):
        """
        Run the backtesting process.
        This method will iterate through the data, generate signals, and execute trades.
        """
        while self.data_feed.has_next():
            data_point = self.data_feed.next()
            action = self.strategy.generate_action()
            self.history.append(map[action])
            self.portfolioManager.execute_order(action, data_point['Open', self.ticker])
            self.strategy.update_history(data_point)
