import pandas as pd

class DataLoader:
    def __init__(self, dataset):
        self.dataset = dataset

    def load(self) -> pd.DataFrame:
        """
        Load the dataset into a pandas DataFrame.

        :return: DataFrame containing the dataset.
        """
        if isinstance(self.dataset, pd.DataFrame):
            return self.dataset
        elif isinstance(self.dataset, str):
            return pd.read_csv(self.dataset)
        else:
            raise ValueError("Unsupported dataset type. Must be a DataFrame or a file path.")