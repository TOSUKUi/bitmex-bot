import pandas as pd



def ohlcv(symbol, platform, span, since=0, to=0):
    """"
    return histrical data of symbol from datastore
        :param symbol: str symbol name
        :param platform: str platform name
        :param span: str span per bin, 5m 10m, ...
        :param since=0: datetime begin of data period
        :param to=0: datetime end of data period 
    """     
    bins = pd.read_csv("bins_data/{}.csv".format(platform))
    resampled_bins = resample_span(bins, span)
    if since == 0:
    return resampled_bins

def resample_span(bins, span):
    """
    resample span
        :param bins: pd.DataFrame 
        :param span: str
    """
    permit_span = ["1min, 5min, 10min, 15min, 30min, 45min, 1h, 2h, 3h, 4h, 6h, 1d"]
    if span not in permit_span:
        raise Exception("Unpermitted span")
    else:
        return ohlcv2(bins.resample(span))


def ohlcv2(resample):
    return resample.agg({
        "open": "open",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum"
    })
    