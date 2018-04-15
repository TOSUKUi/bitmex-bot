import pandas as pd


def rci3lines(long_itv, mid_itv, short_itv, bins):
    close = list(bins["close"])

    long = rci(long_itv, close)
    mid = rci(mid_itv, close)
    short = rci(short_itv, close)
    return [long, mid, short]


def williams_vix_fix(bins, period):
    wvf = ((highest(bins["close"], period) - float(bins.head(1)["low"]))/(highest(bins["close"], period))) * 100
    return wvf


def reverse_williams_vix_fix(bins, period):
    wvf = ((bins.head(1)["high"][0] - lowest(bins["close"], period)) / lowest(bins["close"], period)) * 100
    return wvf


def ord(seq, idx, itv):
    p = seq[idx]
    o = 1
    for i in range(0, itv):
        if p < seq[i]:
            o = o + 1
    return o


def d(itv, src):
    total = 0.0
    for i in range(0, itv):
        total += pow((i + 1) - ord(src, i, itv), 2)
    return total


def highest(src, period):
    return max(src.head(period))


def lowest(src, period):
    return min(src.head(period))


def rci(itv, src):
    return (1.0 - 6.0 * d(itv, src) / (itv * (itv * itv - 1.0))) * 100.0


def crossover(src, val):
    if src[0] > val and src[1] <= val:
        return True
    else:
        return False


def crossunder(src, val):
    if src[0] < val and src[1] >= val:
        return True
    else:
        return False
