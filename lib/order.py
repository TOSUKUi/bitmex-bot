import ccxt
import sys
from lib import api_connecter as connector
import pandas as pd
from datetime import datetime
import time
import logging
from lib import logger as logger
from ccxt.base.errors import NetworkError, AuthenticationError, OrderNotFound, InsufficientFunds
import traceback

class Order():

    def __init__(self, bot_id, api_credential, trading_platform, symbol="BTC/USD", test=False):
        self.client = None
        if test:
            self.client = connector.test_connection(api_credential, trading_platform)
        else:
            self.client = connector.main_connection(api_credential, trading_platform)
        self.test = test
        self.symbol = symbol
        self.bot_id = bot_id
        self.trading_file = "trading_data/{bot_id}_trading_logs.csv".format(bot_id=bot_id)

    def send_order(self, amount, side, price=None):    
        try:
            result = {}
            if price is not None:
                logging.info("create limit buy order...")
                result = self.client.create_order(self.symbol, 'limit', amount=amount, price=price, side=side)
            else:
                logging.info("create market buy order...")
                result = self.client.create_order(self.symbol, 'market', amount=amount, side=side)
            del result["info"]
            self.save_result(result)
        except NetworkError as e:
            time.sleep(30)
            logging.error("DDOS protection occured,\n {}".format(traceback.format_tb(e.__traceback__)))
            self.send_order(amount, side, price)
        except AuthenticationError as e:
            logging.error("Authentication error occured, make sure your account information\n {}".format(traceback.format_tb(e.__traceback__)))
            exit(1)
        except OrderNotFound as e:
            logging.error("Order not found occured, make sure your account information\n {}".format(traceback.format_tb(e.__traceback__)))
            exit(1)
        except InsufficientFunds as e:
            logging.error("InsufficeientFunds" + traceback.format_tb(e.__traceback__)) 
            exit(1)
        
        
    def send_close_order(self):
        try:
            logging.info("close position...")
            response = self.client.private_post_order_closeposition({"symbol": "XBTUSD"})
            result = self.client.parse_order(response, market={"symbol": "BTC/USD"})
            del result["info"]
            self.save_result(result)
            """
            plz tell me exception good pattern
            """
        except NetworkError as e:
            time.sleep(30)
            logging.error("DDOS protection occured,\n {}".format(traceback.format_tb(e.__traceback__)))
            self.send_close_order()
        except AuthenticationError as e:
            logging.error("Authentication error occured, make sure your account information\n {}".format(traceback.format_tb(e.__traceback__)))
            exit(1)
        except OrderNotFound as e:
            logging.error("Order not found occured, make sure your account information\n {}".format(traceback.format_tb(e.__traceback__)))
            exit(1)
      
        
    # def create_stop_order(self, amount, id, stop_offset):
    #     params = {'type': 'Stop', "stopPx": stop_offset}
    def save_result(self, result):
        df = self.__trading_data()
        df = df.append(result, ignore_index=True)
        df.to_csv(self.trading_file)
        del df

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
