import ccxt
import lib.bitmex_api_connecter as connector
import pandas as pd
from datetime import datetime

class Order():
    def __init__(self, bot_id, symbol="BTC/USD", test=False):
        self.client = None
        if test:
            self.client = connector.test_connection(bot_id)
        else:
            self.client = connector.main_connection(bot_id)
        self.test = test
        self.symbol = symbol
        self.bot_id = bot_id
        self.trading_file = "trading_data/{bot_id}_trading_logs.csv".format(bot_id=bot_id)

    def send_order(self, amount, side, price=None):
        try:
            df = pd.read_csv(self.trading_file)
        except:
            df = pd.DataFrame()
        result = {}
        if price is not None:
            result = self.client.create_limit_order("BTC/USD", side=side, amount=amount, price=price)
        else:
            result = self.client.create_market_order("BTC/USD", side=side, amount=amount)
        del result["info"]
        df.append(result)

    #def close_position(self, id):
    def create_stop_order(self, amount, id):
        params = {'type': 'Stop', "stopPx": -50}

