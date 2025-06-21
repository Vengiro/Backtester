from os.path import exists

import pandas as pd
import os

class DataLoader:
    def __init__(self, ticker, period, use_saved_data=True):
        self.ticker = ticker
        self.period = period
        self.use_saved_data = use_saved_data

    def load(self) -> pd.DataFrame:
        """
        Load historical data for a given ticker and period.
        If the data is not available locally, download it using yfinance.

        :return: DataFrame containing historical stock data.
        """
        filename = f"datacache/{self.ticker}_{self.period}.parquet"

        if self.use_saved_data and os.path.exists(filename):
            print(f"Loading data from {filename}")
            dataset = pd.read_parquet(filename)
        else:
            import yfinance as yf
            print(f"Downloading data for {self.ticker} for the period {self.period}")
            dataset = yf.download(self.ticker, period=self.period)
            if not dataset.empty:
                os.mkdir("datacache") if not os.path.exists("datacache") else None
                dataset.to_parquet(filename)
                print(f"Data saved to {filename}")
        return dataset