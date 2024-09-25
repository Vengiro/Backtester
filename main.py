from my_backtesting_project.data_processing import get_historical_data
from my_backtesting_project.display import plot_data


def main():
    data = get_historical_data("AAPL", "2021-01-01", "2021-12-31")
    plot_data(data, "AAPL Stock Price")

if __name__ == "__main__":
    main()