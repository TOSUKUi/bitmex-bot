

def execute(bins, client=None):
    """
    :param bins: dataframe 1 mins  
    :return: 
    """

    pass


def trailing_start(client=None):
    """
    :param  
    :return: 
    """
    if client is not None:
        client.create_market_sell_order("BTC/USD", amount=-1000, params={'type': 'Stop', "stopPx": -50})


    pass


def stop_loss():
    pass