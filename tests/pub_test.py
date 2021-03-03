import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Bramble", 5, 2, 20)
        self.drink2 = Drink("Long Vodka", 10, 3, 10)
        self.food1 = Food("Burger", 20, -4, 10)
        self.food2 = Food("Pizza", 10, -6, 30)

        drinks = [self.drink1, self.drink2]
        food = [self.food1, self.food2]
        self.pub = Pub("The Vaccine Arms", 1500.00, drinks, food)

    def test_pub_name(self):
        self.assertEqual("The Vaccine Arms", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(1500, self.pub.till)
    
    def test_till_transaction(self):
        self.pub.till_transaction(100)
        self.assertEqual(1600, self.pub.till)

    def test_get_drink_name(self):
        find_drink = self.pub.find_drink_by_name("Long Vodka")
        self.assertEqual("Long Vodka", find_drink.name)

    def test_sell_drink_to_customer(self):
        customer = Customer("Bob", 100.00, 25, 5)
        self.pub.sell_drink(customer, "Bramble")
        self.assertEqual(1505.00, self.pub.till)
        self.assertEqual(95.00, customer.wallet)

    def test_sell_drink_to_customer_drink_not(self):
        customer = Customer("Bob", 100.00, 25)
        self.pub.sell_drink(customer, "Beer")
        self.assertEqual(1500.00, self.pub.till)
        self.assertEqual(100.00, customer.wallet)

    def test_sell_drink_to_customer_drink_found_no_funds(self):
        customer = Customer("Bob", 3.00, 25)
        self.pub.sell_drink(customer, "Bramble")
        self.assertEqual(1500.00, self.pub.till)
        self.assertEqual(3.00, customer.wallet)

    def test_sell_drink_to_customer_underage(self):
        customer = Customer("Bob", 100.00,8)
        self.pub.sell_drink(customer, "Bramble")
        self.assertEqual(1500.00, self.pub.till)
        self.assertEqual(100.00, customer.wallet)
    
    def test_sell_drink_to_customer_drunk(self):
        customer = Customer("Bob", 100.00, 25, 15)
        self.pub.sell_drink(customer, "Bramble")
        self.assertEqual(1500.00, self.pub.till)
        self.assertEqual(100.00, customer.wallet)

    def test_sell_food_to_customer_decrease_drunk_level(self):
        customer = Customer("Bob", 100.00, 25, 10)
        self.pub.sell_food(customer, "Pizza")
        self.assertEqual(4, customer.drunk_level)

    def test_access_dict(self):
        item = self.pub.stock["drinks"][1]
    
    def test_stock_value(self):
        self.assertEqual(700, self.pub.check_stock_value())