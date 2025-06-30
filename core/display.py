import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data: pd.DataFrame, trades: list, title: str):
    """
    Plot the given data with a specified title.

    :param data: DataFrame containing the data to plot.
    :param title: Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.plot(data.index, data['Open'], label='Open Price', linestyle='--')

    # Extract buy/sell positions
    buy_signals = data['Close'][[i for i, x in enumerate(trades) if x == 1]]
    sell_signals = data['Close'][[i for i, x in enumerate(trades) if x == -1]]

    # Plot buy/sell signals
    plt.scatter(buy_signals.index, buy_signals.values, marker='^', color='green', label='Buy Signal', zorder=5)
    plt.scatter(sell_signals.index, sell_signals.values, marker='v', color='red', label='Sell Signal', zorder=5)

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()