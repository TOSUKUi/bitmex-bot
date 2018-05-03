from ccxt.bitmex import ExchangeError
class Logic:

    def __init__(self, bins, conditions):
        """
        :param bins: source ohlcv recently 500bins
        :param conditions: condition of logic
        """
        self.bins = bins
        self.conditions = conditions

    def logic_execute(self):
        """
        :return: if execute over then true else false (e.g error occured)
        :rtype: bool
        """
        try:
            self.execute()
        except ExchangeError:
            sleep(200)
            self.logic_execute()




    def execute(self):
        pass