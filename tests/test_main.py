"""Unit tests for the beginner shopping basket exercise."""
import unittest

from main import calculate_total


class ShoppingBasketTests(unittest.TestCase):
    def test_demo_basket(self):
        self.assertEqual(calculate_total({"apple": 0.75, "egg": 0.50}, {"apple": 1, "egg": 6}), 3.75)

    def test_empty_basket(self):
        self.assertEqual(calculate_total({"apple": 1.25}, {}), 0.0)

    def test_unknown_item(self):
        with self.assertRaises(KeyError):
            calculate_total({"apple": 1}, {"pear": 1})

    def test_negative_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total({"apple": 1}, {"apple": -1})

    def test_boolean_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total({"apple": 1}, {"apple": True})


if __name__ == "__main__":
    unittest.main()
