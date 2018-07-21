from lib import order, fetcher
from logic import *
import yaml

ENTRY_OPERATION = ["Buy", "Sell"]
EXIT_OPERATION = ["Close"]
PASS_OPERATION = ["Nothing"]


def read_configration():
    f = open('bot_management.yml', 'r')
    configrations = yaml.load(f.read())
    return configrations


if __name__ == "__main__":
    config = read_configration()
    order_obj = order.Order(config["bot_id"], config["api_credential"], config["trading_platform"], config["symbol"], config["test"])
    ohlcv = fetcher.ohlcv(symbol=config["symbol"], platform=config["trading_platform"], span=config["legs_span"])
    operation = eval(config["logic"])
    if operation in ENTRY_OPERATION:
        order_obj.send_order(config["trade_amount"], operation)
    elif operation in PASS_OPERATION:
        pass
    elif operation in EXIT_OPERATION:
        order_obj.send_close_order()
    else: 
        raise Exception("Operation which logic returned is invalid")
