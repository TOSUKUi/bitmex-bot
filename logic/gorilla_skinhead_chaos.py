import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector
import lib.technical_analysis as ta
import pandas as pd
from datetime import datetime
import logging


logging.basicConfig()

def execute(bins, conditions, client=None):
    # Series set up
    # ema fast

    ma_fast = ta.ema(bins[conditions.ema_fast_source].sort_index(), conditions.ema_fast_length).sort_index(ascending=False)
    # ema slow
    ma_slow = ta.ema(bins[conditions.ema_slow_source].sort_index(), conditions.ema_slow_length).sort_index(ascending=False)

    # print("fast:", ma_fast[0:10], "\nslow:", ma_slow[0:10])
    # print("long", long_entry(ma_fast, ma_slow), "short", short_entry(ma_fast, ma_slow))
    if long_entry(ma_fast, ma_slow):
        if client is not None:
            client.create_market_buy_order("BTC/USD", 1000)
        print("buy", float(bins.head(1)["close"]), "at", bins.index[0].strftime("%Y-%m-%d %H:%M:%S"))
        return True
    elif short_entry(ma_fast, ma_slow):
        if client is not None:
            client.create_market_sell_order("BTC/USD", 1000)
        print("sell", ":price on", float(bins.head(1)["close"]), "at", bins.index[0].strftime("%Y-%m-%d %H:%M:%S"))
        return True
    # print("何もしない", datetime.fromtimestamp(bins.head(1)["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S"))
    return False


def long_entry(ma_fast, ma_slow):
    return ta.crossover(ma_fast, ma_slow)


def short_entry(ma_fast, ma_slow):
    return ta.crossunder(ma_fast, ma_slow)

