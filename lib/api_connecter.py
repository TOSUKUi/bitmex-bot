import ccxt
import yaml


def test_connection(api_credential, trading_platform):
    credential = api_credential["test_net"]
    platform = trading_platform
    exchange = getattr(ccxt, platform)(credential)
    if platform=="bitmex": exchange.urls["api"] = exchange.urls["test"]
    return exchange


def main_connection(api_credential, trading_platform):
    credential = api_credential["main_net"]
    platform = trading_platform
    exchange = getattr(ccxt, platform)(credential)
    return exchange