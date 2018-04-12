import pandas as pd


def rci3lines(long_itv, mid_itv, short_itv, bins):
    close = bin["close"]
    long = __rci(long_itv, close)
    mid = __rci(mid_itv, close)
    short = __rci(short_itv, close)
    return long, mid, short


def williams_vix_fix(bin):
    wvf = ""
    return wvf


def __ord(seq, idx, itv):
    p = seq[idx]
    o = 1
    for i in range(itv - 1):
        if p < seq[i]:
            o = o + 1
    return o


def __d(itv, src):
    sum = 0.0
    for i in range(itv - 1):
        sum = sum + pow((i + 1) - __ord(src, i, itv), 2)
    sum


def __rci(itv, src):
    return (1.0 - 6.0 * __d(itv, src) / (itv * (itv * itv - 1.0))) * 100.0 + 100