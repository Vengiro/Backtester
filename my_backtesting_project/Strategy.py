

class Strategy:
    def __init__(self, ticker: str, period: str, balance: float):
        self.backtester = Backtester(ticker, balance)
        self.ticker = ticker
        self.period = period

    def run(self):
        pass