import pandas as pd
from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    Base class for trading strategies.
    All strategies should inherit from this class and implement the generate_signals method.
    """

    def __init__(self):
        """
        Initialize the Strategy class.
        This method can be overridden by subclasses to set up any necessary parameters.
        """
        self.history = pd.DataFrame()

    def update_history(self, data: dict):
        """
        Update the historical data with the latest data point.

        :param data: A dictionary containing the latest data point.
        """
        self.history = pd.concat([ self.history, pd.DataFrame([data]) ], ignore_index=True)


    @abstractmethod
    def generate_order(self) -> list[dict]:
        """
        Generate trading signals based on the provided data.
        This method should be implemented by subclasses.

        :param data: DataFrame containing historical price data
        :return: DataFrame with signals added
        """
        pass


