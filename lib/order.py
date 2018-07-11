import ccxt
import sys
from lib import bitmex_api_connecter as connector
import pandas as pd
from datetime import datetime
import time
import logging
from lib import logger as logger
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import DDoSProtection
import traceback

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
        df = self.__trading_data()
        try:
            result = {}
            if price is not None:
                logging.info("create limit buy order...")
                result = self.client.create_order(self.symbol, 'limit', amount=amount, price=price, side=side)
            else:
                logging.info("create market buy order...")
                result = self.client.create_order(self.symbol, 'market', amount=amount, side=side)
            del result["info"]
            df = df.append(result, ignore_index=True)
            df.to_csv(self.trading_file)
        except ExchangeError as e:
            time.sleep(10)
            logging.error("some exchange exception occured, \n {}".format(traceback.format_tb(e.__traceback__)))
            self.send_order(self, amount, side, price=price)
        except DDoSProtection:
            time.sleep(60)
            logging.error("DDOS protection occured,\n {}".format(traceback.format_tb(e.__traceback__)))
            self.send_order(self, amount, side, price=price)
        except AuthenticationError as e:
            logging.error("Authentication error occured, make sure your account information\n {}".format(traceback.format_tb(e.__traceback__)))
            exit(1)
        except OrderNotFound as e:
            logging.error("Order not found occured, make sure your account information\n {}".format(traceback.format_tb(e.__traceback__)))
            exit(1)
        del df

    def send_close_order(self):
        df = self.__trading_data()
        logging.info("close position...")
        response = self.client.private_post_order_closeposition({"symbol": "XBTUSD"})
        result = self.client.parse_order(response, market={"symbol": "BTC/USD"})
        del result["info"]
        df = df.append(result, ignore_index=True)
        df.to_csv(self.trading_file)
        del df


    # def create_stop_order(self, amount, id, stop_offset):
    #     params = {'type': 'Stop', "stopPx": stop_offset}



    def __trading_data(self):
        try:
            df = pd.read_csv(self.trading_file, index_col=0)
        except:
            columns = [
                'id',
                'timestamp',
                'datetime',
                'lastTradeTimestamp',
                'symbol',
                'type',
                'side',
                'price',
                'amount',
                'cost',
                'filled',
                'remaining',
                'status',
                'fee'
                ]
            df = pd.DataFrame({}, columns=columns)
        return df
