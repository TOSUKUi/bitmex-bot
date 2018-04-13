from logic import vix_and_rci
from lib.bitmex_api_connecter import test_connection
import pandas as pd
import lib.technical_analysis as ta

if __name__ == "__main__":
    bitmex = test_connection()
    # their max is 500, default is 100 candles
    limit = 500
    since = bitmex.milliseconds() - limit * 300 * 500
    bins = bitmex.fetch_ohlcv('BTC/USD', timeframe="5m", since=since, limit=limit)
    df = pd.DataFrame(bins)
    ta.williams_vix_fix(df, 9)

    print(df)
