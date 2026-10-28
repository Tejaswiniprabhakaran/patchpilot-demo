"""Prices for a shopping basket."""


def apply_discount(price: float, percent: float) -> float:
    """Price after a percentage discount, rounded to two decimals."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def basket_total(prices: list[float]) -> float:
    """Sum of all prices in the basket, rounded to two decimals."""
    total = 0.0
    for i in range(len(prices)):
        total += prices[i]
    return round(total, 2)


def most_expensive(prices: list[float]) -> float:
    """The highest price in a non-empty basket."""
    if not prices:
        raise ValueError("empty basket")
    return max(prices)
