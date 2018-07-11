import ccxt
import yaml


def test_connection(bot_id):
    f = open("bitmex_api_credential.yml", "r")
    data = yaml.load(f)
    f.close()
    bitmex = ccxt.bitmex(data["test_net"])
    bitmex.urls["api"] = bitmex.urls["test"]
    return bitmex


def main_connection(bot_id):
    f = open("bitmex_api_credential.yml", "r")
    data = yaml.load(f)
    f.close()
    bitmex = ccxt.bitmex(data["main_net"])
    return bitmex