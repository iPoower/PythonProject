"""Basic Python exercise: calculate the price of a shopping basket.

Run: python3 main.py
"""
from __future__ import annotations

from collections.abc import Mapping


def calculate_total(prices: Mapping[str, float], quantities: Mapping[str, int]) -> float:
    """Return the total rounded to cents; reject missing items and invalid quantities."""
    total = 0.0
    for item, quantity in quantities.items():
        if item not in prices:
            raise KeyError(f"Unknown item: {item}")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            raise ValueError(f"Invalid quantity for {item}: {quantity!r}")
        if prices[item] < 0:
            raise ValueError(f"Negative price for {item}")
        total += prices[item] * quantity
    return round(total, 2)


def main() -> None:
    prices = {"apple": 0.75, "egg": 0.50}
    basket = {"apple": 1, "egg": 6}
    print(f"I have to pay ${calculate_total(prices, basket):.2f}")


if __name__ == "__main__":
    main()
