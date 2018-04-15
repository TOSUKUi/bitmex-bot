import pandas as pd
import lib.technical_analysis as ta

class VixAndRciCondition:

    def __init__(
            self,
            short_interval, middle_interval, long_interval,
            source,
            high_line, low_line,
            look_back_period_of_standard_deviation_high,
            bolinger_band_length,
            n_sigma,
            look_back_period_percentile_high,
            highest_percentile, lowest_percentile,
            rci_overbought_trigger, rci_oversold_trigger
    ):

        self.short_interval = short_interval
        self.middle_interval = middle_interval
        self.long_interval = long_interval
        self.source = source
        self.high_line = high_line
        self.low_line = low_line
        self.look_back_period_of_standard_deviation_high = look_back_period_of_standard_deviation_high
        self.bolinger_band_length = bolinger_band_length
        self.n_sigma = n_sigma
        self.look_back_period_percentile_high = look_back_period_percentile_high
        self.highest_percentile = highest_percentile
        self.lowest_percentile = lowest_percentile
        self.rci_overbought_trigger = rci_overbought_trigger
        self.rci_oversold_trigger = rci_oversold_trigger

    def is_overbought(self, vrci, wvf):
        wvf_condition = self.__wvf_condition(wvf)

        if wvf_condition == 0:
            return False
        elif wvf_condition == 1 and self.__rci_overbought(vrci):
            return True

    def is_oversold(self, vrci, wvf):
        wvf_condition = self.__wvf_condition(wvf)
        if wvf_condition == 0:
            return False
        elif wvf_condition == 2 and self.__rci_oversold(vrci):
            return True

    def __wvf_condition(self, wvf):
        std_dev = self.n_sigma * wvf.head(self.bolinger_band_length).std()
        mid_line = wvf.head(self.bolinger_band_length).mean()
        lower_band = mid_line - std_dev
        upper_band = mid_line - std_dev
        range_high = ta.highest(wvf, self.look_back_period_percentile_high) * self.highest_percentile
        range_low = ta.lowest(wvf, self.look_back_period_percentile_high) * self.lowest_percentile
        if wvf[0] >= upper_band or wvf[0] >= range_high:
            return 1
        elif wvf[0] <= lower_band or wvf[0] <= range_low:
            return 2
        else:
            return 0

    # def __wvf_overbought_condition(self, wvf):


    def __rci_overbought(self, rci):
        if ta.crossover(rci, self.high_line):
            return True
        else:
            return False

    def __rci_oversold(self, rci):
        if ta.crossunder(rci, self.low_line):
            return True
        else:
            return False
