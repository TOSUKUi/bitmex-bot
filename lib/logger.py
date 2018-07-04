import logging

def get_logger():
    logging.basicConfig(filename="log/{bot_id}.log", format='%(levelname)s :%(asctime)s %(message)s', level=logging.DEBUG)
    logging.getLogger()