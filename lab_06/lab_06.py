# lab_06.py
from money import Coin, CopperCoin, SilverCoin, GoldCoin, Wallet, COPPER, SILVER, GOLD

# Testing the base Coin class
base_coin = Coin(material="iron", value=5)
base_coin.describe()
base_coin.get_coins(10)
base_coin.spend_coins(3)
base_coin.count()

print("=====================")

# Testing CopperCoin
copper_coin = CopperCoin()
copper_coin.describe()
copper_coin.get_coins(15)
copper_coin.spend_coins(5)
copper_coin.count()

print("=====================")

# Testing SilverCoin
silver_coin = SilverCoin()
silver_coin.describe()
silver_coin.get_coins(10)
silver_coin.spend_coins(3)
silver_coin.count()

print("=====================")

# Testing GoldCoin
gold_coin = GoldCoin()
gold_coin.describe()
gold_coin.get_coins(5)
gold_coin.spend_coins(1)
gold_coin.count()

print("=====================")

# Testing Wallet
wallet = Wallet()
wallet.count_money()
wallet.add_coins(COPPER, 10)
wallet.add_coins(SILVER, 5)
wallet.add_coins(GOLD, 2)
wallet.count_money()

print("=====================")

wallet.take_coins(COPPER, 3)
wallet.take_coins(SILVER, 2)
wallet.take_coins(GOLD, 1)
wallet.count_money()