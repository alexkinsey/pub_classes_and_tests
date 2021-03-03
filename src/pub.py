class Pub:
    def __init__(self, name, till, drinks, food):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.food = food
        self.stock = {
            "drinks": drinks,
            "food": food
            } 

    def till_transaction(self, amount):
        self.till += amount

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
        return None
    
    def sell_drink(self, customer, drink_name):
        if customer.age < 18:
            return
        
        if customer.drunk_level > 10:
            return

        drink = self.find_drink_by_name(drink_name)
        if not drink:
            return

        if customer.wallet < drink.price:
            return
        customer.reduce_wallet(drink.price)
        customer.increase_or_decrease_drunk_level(drink.alcohol_level)
        self.till_transaction(drink.price)
    
    def find_food_by_name(self, name):
        for food in self.food:
            if food.name == name:
                return food
        return None

    def sell_food(self, customer, food_name):

        food = self.find_food_by_name(food_name)
        if not food:
            return

        if customer.wallet < food.price:
            return
        customer.reduce_wallet(food.price)
        customer.increase_or_decrease_drunk_level(food.alcohol_level)
        self.till_transaction(food.price)

    def check_stock_value(self):
        #item = self.pub.stock["drinks"][1]
        total = 0
        for drink in self.stock["drinks"]:
            total += drink.price * drink.stock
        for food in self.stock["food"]:
            total += food.price * food.stock

        return total