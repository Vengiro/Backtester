from my_backtesting_project.Strategy import Strategy
from my_backtesting_project.data_processing import get_historical_data
from my_backtesting_project.display import plot_data
import argparse
import matplotlib.pyplot as plt

def main(args):
    """
    strategy = Strategy("AAPL", "1d", 1000)
    strategy.run()
    data = get_historical_data("AAPL", "2021-01-01", "2021-12-31")
    plot_data(data, "AAPL Stock Price")
    """
    plt.figure()
    plt.title('Sketch')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", type=str, help="The stock ticker to backtest", default="AAPL")
    parser.add_argument("--period", type=str, help="The period of the data", default="1d")
    parser.add_argument("--balance", type=float, help="The initial balance", default=1000)
    main(parser.parse_args())