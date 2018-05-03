import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector
import pandas as pd
import time
from tqdm import tqdm

bitmex = connector.back_test_connection()
columns = ["timestamp", "open", "high", "low", "close", "volume"]
df = pd.DataFrame(columns=columns)
limit = 500
mins = 5
length = 220
now = bitmex.milliseconds()
pbar = tqdm(total=length-1)
for i in range(1, length):
    pbar.update(1)
    since = now - (limit - 1) * mins * 60 * 1000 * i
    ohlcv = pd.DataFrame(bitmex.fetch_ohlcv("BTC/USD", timeframe="{}m".format(mins), limit=limit, since=since), columns=columns).sort_values(by = "timestamp", ascending=False)
    df = pd.concat([df, ohlcv], ignore_index=True)
    time.sleep(1)
data_name = "back_test/test_data_xbt_usd_{}min_{}bins.pickle".format(mins, length*limit)
df.to_pickle(data_name)