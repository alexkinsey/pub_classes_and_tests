class Pub:
    def __init__(self, name, till, drinks, food):
        self.name = name
        self.till = till
        self.stock = {
            "drinks": drinks,
            "food": food
            } 

    # add or remove cash from till using positive or negative amount
    def till_transaction(self, amount):
        self.till += amount

    # find any item, must pass key for item_type (food or drinks) as a string
    def find_item_by_name(self, item_type, item_name):
        for item in self.stock[item_type]:
            if item.name == item_name:
                return item
        return None

    # sell any stocked item if customer meets conditions
    def sell_item(self, customer, item_type, item_name, amount = 1):
        item = self.find_item_by_name(item_type, item_name)

        if customer.age < 18 or customer.drunk_level > 10 or not item or customer.wallet < item.price * amount:
            return "could not sell item"
        if self.check_stock_amount(item_type, item.name) < amount:
            return "no stock"

        customer.reduce_wallet(item.price * amount)
        customer.increase_or_decrease_drunk_level(item.alcohol_level * amount)
        self.till_transaction(item.price * amount)
        self.change_stock_amount(item_type, item.name, - amount)

    # check total value of stock and return value
    def check_stock_total_value(self):
        total = 0
        
        for drink in self.stock["drinks"]:
            total += drink.price * drink.stock
        for food in self.stock["food"]:
            total += food.price * food.stock

        return total

    # change the stock amount by passing positive or negative amount
    def change_stock_amount(self, item_type, item_name, amount):
        for i in range(len(self.stock[item_type])):
            if self.stock[item_type][i].name == item_name:
                 self.stock[item_type][i].stock += amount
                 
    # return stock value of an item
    def check_stock_amount(self, item_type, item_name):
        for i in range(len(self.stock[item_type])):
            if self.stock[item_type][i].name == item_name:
                return self.stock[item_type][i].stock
    