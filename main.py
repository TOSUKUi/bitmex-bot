from lib.bitmex_api_connecter import test_connection
from lib.logger import get_logger
import pandas as pd
from logic import vix_and_rci
from logic.conditions.vix_and_rci_condition import VixAndRciCondition
import argparse

logger = get_logger()


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', "--timeframe", type=int, help='足の幅を入力してください')
    return parser.parse_args()


def get_bins(timeframe):
    allow_case = ["1m", "5m", "15m", "30m", "45m", "1h", "4h", "1d"]
    limit = 500
    since = bitmex.milliseconds() - limit * 300 * 1000
    df = None
    if timeframe not in allow_case:
        logger.error("タイムフレームの形式は{}に限ります".format(allow_case))
        raise Exception("タイムフレームの形式が間違っています")
    if timeframe == "15m":
        bins = bitmex.fetch_ohlcv('BTC/USD', timeframe="5m", since=since, limit=limit)
        df = pd.DataFrame(bins[1:], columns=["timestamp", "open", "high", "low", "close", "volume"]).sort_values(
            by="timestamp", ascending=False)
        df.index = list(range(0, len(bins)))
        df.resample("15min", on="datetime").agg({"open": 'first', "high": "max", "low": "min", "close": "last", "volume": "sum"})
    elif timeframe == "30m":
        bins = bitmex.fetch_ohlcv('BTC/USD', timeframe="5m", since=since, limit=limit)
        df = pd.DataFrame(bins[1:], columns=["timestamp", "open", "high", "low", "close", "volume"]).sort_values(
            by="timestamp", ascending=False)
        df.index = list(range(0, len(bins)))
        df.resample("30min", on="datetime").agg(
            {"open": 'first', "high": "max", "low": "min", "close": "last", "volume": "sum"})
    elif timeframe == "45m":
        bins = bitmex.fetch_ohlcv('BTC/USD', timeframe="5m", since=since, limit=limit)
        df = pd.DataFrame(bins[1:], columns=["timestamp", "open", "high", "low", "close", "volume"]).sort_values(
            by="timestamp", ascending=False)
        df.index = list(range(0, len(bins)))
        df.resample("45min", on="datetime").agg(
            {"open": 'first', "high": "max", "low": "min", "close": "last", "volume": "sum"})
    elif timeframe == "4h":
        bins = bitmex.fetch_ohlcv('BTC/USD', timeframe="1h", since=since, limit=limit)
        df = pd.DataFrame(bins[1:], columns=["timestamp", "open", "high", "low", "close", "volume"]).sort_values(
            by="timestamp", ascending=False)
        df.index = list(range(0, len(bins)))
        df.resample("4hour", on="datetime").agg(
            {"open": 'first', "high": "max", "low": "min", "close": "last", "volume": "sum"})
    else:
        bins = bitmex.fetch_ohlcv('BTC/USD', timeframe=timeframe, since=since, limit=limit)
        df = pd.DataFrame(bins[1:], columns=["timestamp", "open", "high", "low", "close", "volume"]).sort_values(
            by="timestamp", ascending=False)
        df.index = list(range(0, len(bins)))
    return df


if __name__ == "__main__":

    bitmex = test_connection()
    timeframe = args_parse()
    df = get_bins(timeframe)


