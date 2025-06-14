

class Strategy:
    """
    Base class for trading strategies.
    All strategies should inherit from this class and implement the generate_signals method.
    """

    def generate_signals(self, data):
        """
        Generate trading signals based on the provided data.
        This method should be implemented by subclasses.

        :param data: DataFrame containing historical price data
        :return: DataFrame with signals added
        """
        raise NotImplementedError("Subclasses must implement this method.")


