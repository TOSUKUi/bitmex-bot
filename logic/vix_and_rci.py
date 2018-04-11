import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector


bitmex = connector.test_connection()
print(bitmex.id, bitmex.load_markets())
