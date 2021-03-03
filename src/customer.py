class Customer:
    def __init__(self,name,wallet,age, drunk_level = None):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunk_level = drunk_level or 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def increase_or_decrease_drunk_level(self, amount):
        self.drunk_level += amount

        if self.drunk_level < 0:
            self.drunk_level = 0
