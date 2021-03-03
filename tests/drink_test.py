import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Long Island Ice Tea", 8.2,5)

    def test_drink_has_name(self):
        self.assertEqual("Long Island Ice Tea", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(8.2, self.drink.price)