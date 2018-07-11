import logging

def get_logger(bot_id):
    logging.basicConfig(filename="log/{bot_id}.log".format(bot_id), format='%(levelname)s :%(asctime)s %(message)s', level=logging.DEBUG)
    return logging.getLogger()