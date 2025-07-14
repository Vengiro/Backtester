from core.strategy import Strategy
class MeanReversionStrategy(Strategy):
    def __init__(self, window: int = 20, threshold: float = 0.05, ticker: str = "MSFT"):
        super().__init__()
        self.window = window
        self.threshold = threshold
        self.ticker = ticker
        # Add trades that has to be closed to the given price
        self.open_trades = {"buy": [], "sell": []}

    def generate_action(self) -> str:
        if len(self.history) < self.window:
            return "hold"

        prices = self.history['Close', self.ticker]
        moving_avg = prices.rolling(window=self.window).mean()
        current_price = prices.iloc[-1]
        mean_price = moving_avg.iloc[-1]

        deviation = (current_price - mean_price) / mean_price

        # Check if we have open trades that can be closed
        closing_actions = "hold"
        for price in self.open_trades["buy"]:
            if current_price >= price:
                self.open_trades["buy"].remove(price)
                closing_actions = "sell"
        for price in self.open_trades["sell"]:
            if current_price <= price:
                self.open_trades["sell"].remove(price)
                closing_actions = "buy" if closing_actions == "hold" else "hold"

        if deviation < -self.threshold:
            self.open_trades["sell"].append(current_price + self.threshold * mean_price)  # Expecting price to rise
            return "buy"   # Price is too low, expect mean reversion up
        elif deviation > self.threshold:
            self.open_trades["buy"].append(current_price - self.threshold * mean_price)
            return "sell"  # Price is too high, expect mean reversion down
        else:
            return "hold"