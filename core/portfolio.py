
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


class PortfolioManager:
    def __init__(self, portfolio: Portfolio, exposure: float = 0.1):
        """
        Initialize the PortfolioManager with a Portfolio instance.
        """
        self.portfolio = portfolio
        self.exposure = exposure

    def execute_order(self, action: str,  price: float):
        """
        Execute an order on the portfolio.

        :param order: Order to be executed, should be a dictionary with 'type' and 'amount'.
        """
        if action == "buy":
            order = {"type": "buy", "amount": self.portfolio.cash * self.exposure}
        elif action == "sell":
            order = {"type": "sell", "amount": self.portfolio.asset * self.exposure}
        else:
            return
        self.portfolio.execute(order, price)

    def get_portfolio_value(self, price: float) -> float:
        """
        Get the total value of the portfolio.

        :param price: Current price of the asset.
        :return: Total value of the portfolio.
        """
        return self.portfolio.get_value(price)