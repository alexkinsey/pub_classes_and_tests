import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Bramble", 5, 2, 20)
        self.drink2 = Drink("Long Vodka", 10, 3, 10)
        self.drink3 = Drink("Martini", 5, 3, 0)
        self.food1 = Food("Burger", 20, -4, 10)
        self.food2 = Food("Pizza", 10, -6, 30)

        drinks = [self.drink1, self.drink2, self.drink3]
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
        find_drink = self.pub.find_item_by_name("drinks", "Long Vodka")
        self.assertEqual("Long Vodka", find_drink.name)

    def test_sell_drink_to_customer(self):
        customer = Customer("Bob", 100.00, 25)
        self.pub.sell_item(customer, "drinks", "Bramble")
        self.assertEqual(1505.00, self.pub.till)
        self.assertEqual(95.00, customer.wallet)
        self.assertEqual(19, self.pub.stock["drinks"][0].stock)

    def test_sell_drink_to_customer_drink__not_exist(self):
        customer = Customer("Bob", 100.00, 25)
        self.assertEqual("could not sell item", self.pub.sell_item(customer, "drinks", "Beer"))

    def test_sell_drink_to_customer_drink_found_no_funds(self):
        customer = Customer("Bob", 3.00, 25)
        self.assertEqual("could not sell item", self.pub.sell_item(customer, "drinks", "Bramble"))

    def test_sell_drink_to_customer_underage(self):
        customer = Customer("Bob", 100.00, 8)
        self.assertEqual("could not sell item", self.pub.sell_item(customer, "drinks", "Bramble"))
    
    def test_sell_drink_to_customer_drunk(self):
        customer = Customer("Bob", 100.00, 25, 9)
        self.pub.sell_item(customer, "drinks", "Bramble")
        self.assertEqual("could not sell item", self.pub.sell_item(customer, "drinks", "Bramble"))

    def test_sell_food_to_customer_decrease_drunk_level(self):
        customer = Customer("Bob", 100.00, 25, 10)
        self.pub.sell_item(customer, "food", "Pizza")
        self.assertEqual(4, customer.drunk_level)

    def test_sell_drink_to_customer_drink_found_no_stock(self):
        customer = Customer("Bob", 18, 25)
        self.assertEqual("no stock", self.pub.sell_item(customer, "drinks", "Martini"))
    
    def test_stock_value(self):
        self.assertEqual(700, self.pub.check_stock_total_value())

    def test_check_stock_amount(self):
        self.assertEqual(20, self.pub.check_stock_amount("drinks", "Bramble"))

    def test_decrease_stock(self):
        self.pub.change_stock_amount("food", "Pizza", -3)
        self.assertEqual(27, self.pub.stock["food"][1].stock)

    def test_sell_item_at_quantity(self):
        customer = Customer("Zac", 100.00, 25)
        self.pub.sell_item(customer, "drinks", "Bramble", 10)
        self.assertEqual(1550, self.pub.till)
