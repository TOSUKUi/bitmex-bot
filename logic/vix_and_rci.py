import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector
import lib.technical_analysis as ta
import pandas as pd
from datetime import datetime

def execute(bins, conditions, client=None):
    #rciの値[long, mid, short]

    rci3lines = [ta.rci3lines(conditions.long_interval, conditions.middle_interval, conditions.short_interval, bins[i:])
                 for i in range(0, 3)]
    df_rci3lines = pd.DataFrame(rci3lines, columns=["long", "mid", "short"])

    wvfs = [ta.williams_vix_fix(bins[i:], conditions.look_back_period_of_standard_deviation_high)
            for i in range(0, conditions.look_back_period_percentile_high + 1)]
    s_wvfs = pd.Series(wvfs)


    # 最低50足分のwvf, 最低2足分のrci
    if conditions.is_overbought(df_rci3lines[conditions.rci_overbought_trigger], s_wvfs):
        if client is not None:
            client.create_market_sell_order("BTC/USD", 1000)
        print("buy", datetime.fromtimestamp(bins.head(1)["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S"))
        return True
    elif conditions.is_oversold(df_rci3lines[conditions.rci_oversold_trigger], s_wvfs):
        if client is not None:
            client.create_market_buy_order("BTC/USD", 1000)
        print("sell", datetime.fromtimestamp(bins.head(1)["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S"))
        return True
    # print("何もしない", datetime.fromtimestamp(bins.head(1)["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S"))
    return False