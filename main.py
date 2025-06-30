from core.strategy import Strategy
from core.backtester import Backtester
from core.display import plot_data
from core.data_loader import DataLoader
from core.portfolio import Portfolio, PortfolioManager
from strategies.simple_MA import SimpleMovingAverageStrategy
import argparse
import yfinance

def main(args):
    strategy = SimpleMovingAverageStrategy(short_window=20, long_window=50)
    data_loader = DataLoader(ticker=args.ticker, period=args.period, use_saved_data=True)
    portfolio = Portfolio()
    portfolio_manager = PortfolioManager(portfolio)
    backtester = Backtester(strategy, data_loader, portfolio_manager, args.ticker)
    backtester.run()
    plot_data(data_loader.load(), backtester.history, f"Chart for {args.ticker}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", type=str, help="The stock ticker to backtest", default="MSFT")
    parser.add_argument("--period", type=str, help="The period of the data", default="60d")
    main(parser.parse_args())