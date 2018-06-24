import ccxt
import lib.bitmex_api_connecter as connector
import pandas as pd

class Order():

    def __init__(self, bot_id, symbol="BTC/USD", test=False):
        self.client = None
        if test == "back_test":
            client = None
        elif test == "test":
            client = connector.test_connection(bot_id)
        elif test is None:
            client = connector.main_connection(bot_id)
        self.test = test
        self.symbol = symbol
        self.bot_id = bot_id
        self.trading_file = "{bot_id}_trading_file.csv".format(bot_id=bot_id)

    def create_buy_order(self, amount, id):
        df = pd.read_csv(self.trading_file)
        positions = df[df["is_closed"] == 0]
        if len(positions) < 1:

            df.append([])


    def create_stop_order(self, amount, id):
        params = {'type': 'Stop', "stopPx": -50}

