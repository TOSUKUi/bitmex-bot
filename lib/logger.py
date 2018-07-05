import logging
from datetime import datetime

def get_logger():
    logging.basicConfig(filename="log/{today}.log".format(today=datetime.now), format='%(levelname)s :%(asctime)s %(message)s', level=logging.DEBUG)
    return logging.getLogger()