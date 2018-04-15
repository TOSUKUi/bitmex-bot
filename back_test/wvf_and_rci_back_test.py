import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector
from logic import vix_and_rci
from logic.conditions.vix_and_rci_condition import VixAndRciCondition
import pandas as pd


df = pd.read_pickle("back_test/test_data_xbt_usd.pickle")
con_vix_and_rci = VixAndRciCondition(
    short_interval=9,
    long_interval=52,
    middle_interval=36,
    rci_overbought_trigger="short",
    rci_oversold_trigger="short",
    source="close",
    high_line=80,
    low_line=-80,
    look_back_period_of_standard_deviation_high=22,
    bolinger_band_length=20,
    n_sigma=4,
    look_back_period_percentile_high=50,
    highest_percentile=0.85,
    lowest_percentile=1.01
)
for i in range(0, len(df)):
    vix_and_rci.execute(df[i:], con_vix_and_rci, client=None)
