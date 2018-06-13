from lib.mysql_connection import *

class Order:

    def __init__(self, client):
        self.client = client


    def create_buy_order(self, symbol="BTC/USD", amount=1000):
        Position()
        try:
            self.client.create_market_buy_order(amount)

        except:

