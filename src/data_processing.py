import yfinance as yf
import matplotlib.pyplot as plt
from src.Strategy import Strategy

class Backtester:
    def __init__(self, ticker: str, balance: float, strategy: Strategy):
        self.ticker = ticker
        self.data = yf.Ticker(ticker).history(period="1d")
        self.data["Return"] = self.data["Close"].pct_change()
        self.data["Cumulative Return"] = (1 + self.data["Return"]).cumprod()
        self.data["Cumulative Return"].plot()
        self.balance = balance
        self.shares = 0
        self.purchases = []
        self.sells = []
        self.strategy = strategy


    def get_historical_data(self, start_date, end_date):
        data = yf.download(ticker, start=start_date, end=end_date)
        return data

    def buy(self, date, amount):
        price = self.data.loc[date, "Close"]
        self.shares += amount / price
        self.balance -= amount
        self.purchases.append(date)

    def sell(self, date, amount):
        price = self.data.loc[date, "Close"]
        self.shares -= amount / price
        self.balance += amount
        self.sells.append(date)

    def run(self):
        self.data = self.strategy.generate_signals(self.data)

        ## TODO Apply signals

