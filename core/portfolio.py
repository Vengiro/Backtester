
class Portfolio:
    def __init__(self, cash: float = 10000.0):
        """
        Initialize the Portfolio with a starting cash amount.

        :param cash: Initial cash available for trading.
        """
        self.cash = cash
        self.asset = 0.0


    def execute(self, order: dict, price: float):
        """
        Execute a trade based on the order type and amount.
        """
        if order["type"] == "buy" and self.cash >= order["amount"] * price:
            self.asset += order["amount"]
            self.cash -= order["amount"] * price

        elif order["type"] == "sell" and self.asset >= order["amount"]:
            self.asset -= order["amount"]
            self.cash += order["amount"] * price


    def get_value(self, price: float) -> float:
        """
        Calculate the total value of the portfolio based on current cash and asset value.

        :param price: Current price of the asset.
        :return: Total value of the portfolio.
        """
        return self.cash + self.asset * price