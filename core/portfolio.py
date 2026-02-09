import pandas as pd
from utils import Position, Order
from collections import defaultdict
class Portfolio:
    def __init__(self, cash: float = 10000.0, fee= 0.001):
        """
        Initialize the Portfolio with a starting cash amount.

        :param cash: Initial cash available for trading.
        """
        self.cash = cash
        self.asset = defaultdict(Position)
        self.fee = fee


    def execute(self, order: Order, price: float):
        """
        Execute a trade based on the order type and amount.
        """
        if order.type == "buy" and self.cash >= order.amount * price:
            self.asset[order.symbol].update(price, order.amount)
            self.cash -= order.amount * price  * (1 + self.fee)

        elif order.type == "sell":
            self.asset[order.symbol].update(price, -order.amount)
            self.cash += order.amount * price * (1 - self.fee)


    def get_value(self, price: float) -> float:
        """
        Calculate the total value of the portfolio based on current cash and asset value.

        :param price: Current price of the asset.
        :return: Total value of the portfolio.
        """
        all_pos = self.asset.values()
        asset_value = sum(pos.get_value(price) for pos in all_pos)
        return self.cash + asset_value



class PortfolioManager:
    def __init__(self, portfolio: Portfolio, exposure: float = 0.1):
        """
        Initialize the PortfolioManager with a Portfolio instance.
        """
        self.portfolio = portfolio
        self.exposure = exposure
        self.history = []
        self.nb_trades = 0
        self.nb_wins = 0
        self.nb_losses = 0

    def execute_order(self, action: str, tick:str,  price: float):
        """
        Execute an order on the portfolio.

        :param order: Order to be executed, should be a dictionary with 'type' and 'amount'.
        """
        if action == "buy":
            order = Order(symbol=tick, type="buy", amount=self.portfolio.cash * self.exposure / price, price=price)
        elif action == "sell":
            order = Order(symbol=tick, type="sell", amount=self.portfolio.asset[tick].amount, price=price)
        else:
            return

        self.portfolio.execute(order, price)
        self.history.append(self.portfolio.get_value(price))

    def get_portfolio_value(self, price: float) -> float:
        """
        Get the total value of the portfolio.

        :param price: Current price of the asset.
        :return: Total value of the portfolio.
        """
        return self.portfolio.get_value(price)

    def compute_metrics(self):
        """
        Compute and return performance metrics of the portfolio.
        """
        df = pd.DataFrame(self.history, columns=["value"])
        df["returns"] = df["value"].pct_change().fillna(0)
        df["cumulative_returns"] = (1 + df["returns"]).cumprod() - 1

        sharp = df["returns"].mean() / df["returns"].std() if df["returns"].std() != 0 else 0

        peak = df["value"].cummax()
        drawdown = (df["value"] - peak) / peak
        max_drawdown = drawdown.min() if not drawdown.empty else 0
        total_return = df["cumulative_returns"].iloc[-1] if not df["cumulative_returns"].empty else 0
        return {
            "total_return": total_return,
            "max_drawdown %": max_drawdown * 100,
            "sharp ratio": sharp,
            "nb_trades": self.nb_trades,
            "nb_wins": self.nb_wins,
            "nb_losses": self.nb_losses
        }
