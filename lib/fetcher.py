import ccxt
from lib.bitmex_api_connecter import *

class Fetcher:

    def __init__(self, environment=None):
        if environment is None:
            self.client = main_connection()
        elif environment == "back_test":
            self.client = main_connection()
        elif environment == "test_net":
            self.client = test_connection()




