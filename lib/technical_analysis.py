import pandas as pd


def rci3lines(long_itv, mid_itv, short_itv, bins):
    close = bins["close"]
    long = __rci(long_itv, close)
    mid = __rci(mid_itv, close)
    short = __rci(short_itv, close)
    return long, mid, short


def williams_vix_fix(bins, period):
    wvf = ((__highest(bins["close"], period)-bins.loc[-1]["low"])/(__highest(bins["close"], period)))
    return wvf


def __ord(seq, idx, itv):
    p = seq[idx]
    o = 1
    for i in range(0, itv):
        if p < seq[i]:
            o = o + 1
    return o


def __d(itv, src):
    total = 0.0
    for i in range(0, itv):
        total += pow((i + 1) - __ord(src, i, itv), 2)
    return total


def __highest(src, span):
    return max(src[:span])

def __rci(itv, src):
    return (1.0 - 6.0 * __d(itv, src) / (itv * (itv * itv - 1.0))) * 100.0 + 100