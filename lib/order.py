import ccxt
import lib.bitmex_api_connecter as connector
import pandas as pd
from datetime import datetime

class Order():

    def __init__(self, bot_id, symbol="BTC/USD", test=False):
        self.client = None
        if test == "back_test":
            self.client = None
        elif test == "test":
            self.client = connector.test_connection(bot_id)
        elif test is None:
            self.client = connector.main_connection(bot_id)
        self.test = test
        self.symbol = symbol
        self.bot_id = bot_id
        self.trading_file = "trading_data/{bot_id}_trading_file.csv".format(bot_id=bot_id)

    def create_order(self, amount, side, price=None):
        df = pd.read_csv(self.trading_file)
        positions = df[df["is_closed"] == 0]
        result = {}
        position = {}
        if len(positions) < 1:
            if self.client is not None:
                if price is not None:
                    result = self.client.create_limit_order("BTC/USD", side=side, amount=amount, price=price)
                else:
                    result = self.client.create_market_order("BTC/USD", side=side, amount=amount)
                position["entry_price"] = result["price"]
                position["is_test"] = 0
            else:
                position["entry_price"] = price
                position["is_test"] = 1
            position["closed"] = 0
            position["entried_at"] = datetime.now()
            position["side"] = side
            position["amount"] = amount
            position["close_price"] = 0
            df.append()





    def create_stop_order(self, amount, id):
        params = {'type': 'Stop', "stopPx": -50}

