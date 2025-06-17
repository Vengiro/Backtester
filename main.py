from core.strategy import Strategy
from core.backtester import Backtester
from core.display import plot_data
from core.data_loader import DataLoader
from core.portfolio import Portfolio, PortfolioManager
from strategies.simple_MA import SimpleMovingAverageStrategy
import argparse
import yfinance

def main(args):
    data = yfinance.download(args.ticker, period=args.period)
    strategy = SimpleMovingAverageStrategy(short_window=20, long_window=50)
    data_loader = DataLoader(data)
    portfolio = Portfolio()
    portfolio_manager = PortfolioManager(portfolio)
    backtester = Backtester(strategy, data_loader, portfolio_manager)
    backtester.run()
    plot_data(data_loader.load(), f"Chart for {args.ticker}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", type=str, help="The stock ticker to backtest", default="AAPL")
    parser.add_argument("--period", type=str, help="The period of the data", default="60d")
    main(parser.parse_args())