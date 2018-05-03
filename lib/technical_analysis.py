import pandas as pd
import numpy as np
from numba import jit

def rci3lines(long_itv, mid_itv, short_itv, bins):
    close = np.array(bins["close"])

    long = rci(long_itv, close)
    mid = rci(mid_itv, close)
    short = rci(short_itv, close)
    return [long, mid, short]


def williams_vix_fix(bins, period):
    high = highest(bins["close"], period)
    wvf = ((high - float(bins.head(1)["low"])) / high) * 100
    return wvf


def reverse_williams_vix_fix(bins, period):
    low = lowest(bins["close"], period)
    wvf = ((float(bins.head(1)["high"]) - low) / low) * 100
    return wvf


def ord(seq, idx, itv):
    p = seq[idx]
    return np.sum(seq[0:itv] < p)


def d(itv, src):
    total = 0.0
    for i in range(0, itv):
        total += pow((i + 1) - ord(src, i, itv), 2)
    return total


def highest(src, period):
    return src.head(period).max()


def lowest(src, period):
    return src.head(period).min()


def rci(itv, src):
    return (1.0 - 6.0 * d(itv, src) / (itv * (itv * itv - 1.0))) * 100.0


def crossover(src1, src2):
    # print("src:", src[0], src[1], "val:", val)
    if src1[0] > src2[0] and src1[1] <= src2[1]:
        return True
    else:
        return False


def crossunder(src1, src2):
    # print("src:", src1[0], src1[1], "src2:", src2[0], src2[1])
    if src1[0] < src2[0] and src1[1] >= src2[1]:
        return True
    else:
        return False


def ema(series, length):
    """
    :param series: pd.Series, a series for get ema 
    :param length: integer, a int for ema period
    :return: 
    """
    return series.ewm(span=length).mean()