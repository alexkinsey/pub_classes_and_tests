class Pub:
    def __init__(self, name, till, drinks, food):
        self.name = name
        self.till = till
        self.stock = {
            "drinks": drinks,
            "food": food
            } 

    def till_transaction(self, amount):
        self.till += amount

    def find_drink_by_name(self, name):
        for drink in self.stock["drinks"]:
            if drink.name == name:
                return drink
        return None
        
    def find_food_by_name(self, name):
        for food in self.stock["food"]:
            if food.name == name:
                return food
        return None

    def sell_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)
        if customer.age < 18 or customer.drunk_level > 10 or not drink or customer.wallet < drink.price:
            return "could not sell drink"

        customer.reduce_wallet(drink.price)
        customer.increase_or_decrease_drunk_level(drink.alcohol_level)
        self.till_transaction(drink.price)
        self.change_stock_amount("drinks", drink.name, -1)


    def sell_food(self, customer, food_name):
        food = self.find_food_by_name(food_name)
        if not food or customer.wallet < food.price:
            return "could not sell food"

        customer.reduce_wallet(food.price)
        customer.increase_or_decrease_drunk_level(food.alcohol_level)
        self.till_transaction(food.price)
        self.change_stock_amount("food", food.name, -1)

    def check_stock_total_value(self):
        total = 0
        
        for drink in self.stock["drinks"]:
            total += drink.price * drink.stock
        for food in self.stock["food"]:
            total += food.price * food.stock

        return total

    def change_stock_amount(self, key, item, amount):
        for i in range(len(self.stock[key])):
            if self.stock[key][i].name == item:
                 self.stock[key][i].stock += amount
                 
    def check_stock_amount(self, key, item):
        for i in range(len(self.stock[key])):
            if self.stock[key][i].name == item:
                return self.stock[key][i].stock
    