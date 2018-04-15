from logic import vix_and_rci
from lib.bitmex_api_connecter import test_connection
import pandas as pd
import lib.technical_analysis as ta
from logic import vix_and_rci
from logic.conditions.vix_and_rci_condition import VixAndRciCondition



if __name__ == "__main__":

    bitmex = test_connection()
    # their max is 500, default is 100 candles

    limit = 500
    since = bitmex.milliseconds() - limit * 300 * 1000

    # 5分感覚で繰り返し
    bins = bitmex.fetch_ohlcv('BTC/USD', timeframe="5m", since=since, limit=limit)
    df = pd.DataFrame(bins[1:], columns=["timestamp", "open", "high", "low", "close", "volume"]).sort_values(by="timestamp", ascending=False)
    df.index = list(range(0, len(bins)))
    vix_and_rci_condition = VixAndRciCondition("条件")
    vix_and_rci.execute(df, vix_and_rci_condition, bitmex)





    #fig = plt.figure()
    #ax = plt.subplot()
    #mpf.candlestick_ochl(ax, df[["timestamp", "open", "high", "low", "close"]])
    #ax.grid()
    #fig.autofmt_xdate()