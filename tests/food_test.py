import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger",12,-2)
    
    def test_food_name(self):
        self.assertEqual("Burger",self.food.name)
    
    def test_food_price(self):
        self.assertEqual(12,self.food.price)

    def test_food_alcohol_level(self):
        self.assertEqual(-2,self.food.alcohol_level)