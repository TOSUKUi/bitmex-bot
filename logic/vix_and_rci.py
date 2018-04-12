import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector
import lib.technical_analysis as ta

def execute(martkets, upperband, lowerband):
    #rciの値[long, mid, short]
    rci3lines = ta.rci3lines(long_itv, mid_itv, short_itv, bins)
    uppderband = upperband
    lowerband = lowerband