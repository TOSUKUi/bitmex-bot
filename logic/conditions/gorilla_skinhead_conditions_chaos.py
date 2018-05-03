class GorillaSkinheadChaos:

    def __init__(self, ema_slow_length, ema_fast_length, ema_fast_source, ema_slow_source):
        self.ema_slow_length = ema_slow_length
        self.ema_fast_length = ema_fast_length
        self.ema_fast_source = ema_fast_source
        self.ema_slow_source = ema_slow_source