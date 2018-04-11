import ccxt
import yaml


def test_connection():
    f = open("bitmex_api_credential.yml", "r")
    data = yaml.load(f)
    f.close()
    print(data)
    bitmex = ccxt.bitmex(data["test_net"])
    return bitmex


if __name__=="__main__":
    test_connection()