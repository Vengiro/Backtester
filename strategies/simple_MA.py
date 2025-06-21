"""
Example of a simple moving average strategy
"""
from core.strategy import Strategy
class SimpleMovingAverageStrategy(Strategy):
    def __init__(self, short_window: int = 20, long_window: int = 50, ticker: str = "MSFT"):
        """
        Initialize the SimpleMovingAverageStrategy with short and long moving average windows.

        :param short_window: The window size for the short moving average.
        :param long_window: The window size for the long moving average.
        """
        super().__init__()
        self.short_window = short_window
        self.long_window = long_window
        self.ticker = ticker


    def generate_action(self) -> str:
        """
        Generate trading signals based on the simple moving average crossover strategy.
        Buy when the short moving average crosses above the long moving average,
        and sell when the short moving average crosses below the long moving average.

        :return: 'buy' or 'sell' signal
        """
        if len(self.history) < self.long_window:
            return "hold"


        # Kinda slow since we are calculating the moving averages every time
        # Ok for backtesting and small datasets, but not for live trading

        short_ma = self.history['Close', self.ticker].rolling(window=self.short_window).mean()
        long_ma = self.history['Close', self.ticker].rolling(window=self.long_window).mean()
        if short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]:
            return "buy"
        elif short_ma.iloc[-1] < long_ma.iloc[-1] and short_ma.iloc[-2] >= long_ma.iloc[-2]:
            return "sell"
        else:
            return "hold"
