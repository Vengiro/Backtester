"""
Example of a simple moving average strategy
"""
class SimpleMovingAverageStrategy(Strategy):
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        data['SMA_Short'] = data['Close'].rolling(self.short_window).mean()
        data['SMA_Long'] = data['Close'].rolling(self.long_window).mean()

        # Create signals column and fill it
        data['Signal'] = 0

        data.loc[data['SMA_Short'] > data['SMA_Long'], 'Signal'] = 1  # Buy
        data.loc[data['SMA_Short'] <= data['SMA_Long'], 'Signal'] = -1  # Sell
        return data
