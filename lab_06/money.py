# Constants
COPPER = "copper"
SILVER = "silver"
GOLD = "gold"

# Base Coin Class
class Coin:
    def __init__(self, material, value, amount=0):
        self.material = material
        self.value = value
        self.amount = amount
    
    def describe(self):
        print(f"This coin is made of {self.material}.")
    
    def get_coins(self, amount):
        self.amount += amount
    
    def spend_coins(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Not enough coins to spend.")
    
    def get_value(self):
        return self.amount * self.value
    
    def count(self):
        total_value = self.get_value()
        print(f"You have {self.amount} {self.material} coins worth {total_value} in total.")

# Coin types
class CopperCoin(Coin):
    def __init__(self):
        super().__init__(COPPER, 1)

class SilverCoin(Coin):
    def __init__(self):
        super().__init__(SILVER, 10)

class GoldCoin(Coin):
    def __init__(self):
        super().__init__(GOLD, 100)

# Wallet Class
class Wallet:
    def __init__(self):
        self.coins = {
            COPPER: CopperCoin(),
            SILVER: SilverCoin(),
            GOLD: GoldCoin()
        }
    
    def count_money(self):
        total_value = 0
        for coin in self.coins.values():
            coin.count()
            total_value += coin.get_value()
        print(f"Total value in wallet: {total_value}")
    
    def add_coins(self, coin_type, amount):
        if coin_type in self.coins:
            self.coins[coin_type].get_coins(amount)
            print(f"Added {amount} {coin_type} coins to the wallet.")
        else:
            print("Invalid coin type.")
    
    def take_coins(self, coin_type, amount):
        if coin_type in self.coins:
            self.coins[coin_type].spend_coins(amount)
            print(f"Removed {amount} {coin_type} coins from the wallet.")
        else:
            print(f"No coin type {coin_type} in wallet.")
