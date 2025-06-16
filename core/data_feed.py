import pandas as pd

class DataFeed:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the DataFeed with a pandas DataFrame.

        :param data: DataFrame containing historical price data.
        """
        self.data = data
        self.index = 0

    def has_next(self) -> bool:
        """
        Check if there are more data points available.

        :return: True if there are more data points, False otherwise.
        """
        return self.index < len(self.data)

    def next(self) -> dict:
        """
        Get the next data point from the DataFeed.

        :return: The next data point as dict
        """

        row = self.data.iloc[self.index]
        self.index += 1
        return row.to_dict()
