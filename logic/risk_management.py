import numpy as np

def execute(bins, condition, client=None):
    """
    :param bins: dataframe 1 mins  
    :return: 
    """



    pass


def trailing_start(amount, side, client=None,):
    """
    :param  
    :return: 
    """
    if client is not None:
        client.create_market_order("BTC/USD", amount=amount, side=side, params={'type': 'Stop', "stopPx": -50})
    


def stop_loss():
    pass


def calc_amount(levarage):
    pass


def profit_out():
    pass
