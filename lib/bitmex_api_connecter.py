import ccxt
import yaml


def test_connection():
    f = open("bitmex_api_credential.yml", "r")
    data = yaml.load(f)
    f.close()
    bitmex = ccxt.bitmex(data["test_net"])
    bitmex.urls["api"] = bitmex.urls["test"]
    return bitmex


def main_connection():
    f = open("bitmex_api_credential.yml", "r")
    data = yaml.load(f)
    f.close()
    bitmex = ccxt.bitmex(data["main_net"])
    return bitmex