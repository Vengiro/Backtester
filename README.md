# Backtesting Framework for Trading Strategies

A lightweight and modular Python framework for backtesting trading strategies using historical stock market data. This project includes components for data loading, strategy execution, portfolio management, and result visualization.

## Features

* Plug-and-play trading strategies (e.g., Moving Average Crossover)
* Modular design for extensibility
* Portfolio and cash management
* Uses Yahoo Finance for historical data
* Command-line interface for quick testing

## Project Structure

```
.
├── core
│   ├── backtester.py          # Main backtester logic
│   ├── data_feed.py           # Iterates over data
│   ├── data_loader.py         # Loads data from CSV or DataFrame
│   ├── display.py             # Plotting utilities
│   ├── portfolio.py           # Portfolio and trade execution logic
│   └── strategy.py            # Base strategy class
├── strategies
│   └── simple_MA.py           # Example strategy: Simple Moving Average
├── main.py                    # Entry point
└── README.md                  # This file
```

## Requirements

* Python 3.8+
* `pandas`
* `matplotlib`
* `yfinance`
* `ccxt`
* `pyarrow`

Install dependencies with:

```bash
poetry install
```

## Usage

Run the backtest from the command line:

```bash
python main.py --ticker AAPL --period 60d
```

* `--ticker`: Stock ticker (e.g., AAPL, MSFT, TSLA)
* `--period`: Time range (e.g., 60d, 1y, 5y)

## Example Output

The script will:

1. Download historical price data from Yahoo Finance.
2. Apply the `SimpleMovingAverageStrategy`.
3. Execute trades via the portfolio manager.
4. Display a price chart.

## Implemented Strategy

**Simple Moving Average Crossover**:

* Buy when short MA crosses above long MA.
* Sell when short MA crosses below long MA.
* Holds otherwise.

You can define your own strategies by subclassing `Strategy`.

## License

This project is open-source and free to use under the MIT License.
