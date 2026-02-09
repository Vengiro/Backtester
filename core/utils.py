from dataclasses import dataclass



@dataclass
class Position:

    """
    A class to represent a trading position.
    """
    symbol: str
    amount: float = 0.0
    avg_price: float = 0.0
    realized_pnl: float = 0.0

    def update(self, price: float, amount: float):
        if self.amount + amount == 0:
            self.realized_pnl += (price - self.avg_price) * self.amount
            self.avg_price = 0.0
        elif self.amount + amount > 0:
            self.avg_price = (self.avg_price * abs(self.amount) + price * abs(amount)) / (
                    abs(self.amount) + abs(amount))

        self.amount += amount

    def get_value(self, price: float) -> float:
        return self.amount * price

    def get_unrealized_pnl(self, price: float) -> float:
        return (price - self.avg_price) * self.amount


@dataclass
class Order:
    """
    A class to represent a trading order.
    """
    symbol: str
    type: str
    amount: float
    price: float