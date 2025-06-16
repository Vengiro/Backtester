import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data: pd.DataFrame, title: str):
    """
    Plot the given data with a specified title.

    :param data: DataFrame containing the data to plot.
    :param title: Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()