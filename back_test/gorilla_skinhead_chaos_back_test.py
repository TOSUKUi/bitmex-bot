import sys
sys.path.append('.')
from logic import gorilla_skinhead_chaos
from logic.conditions.gorilla_skinhead_conditions_chaos import GorillaSkinheadChaos
import pandas as pd
from numba import jit
from tqdm import tqdm
import multiprocessing



def simulation(df, con):
    simulation_length = len(df) - con.ema_slow_length

    for i in tqdm(range(0, simulation_length)):
        gorilla_skinhead_chaos.execute(df[i:], con, client=None)

df = pd.read_pickle("back_test/test_data_xbt_usd_45min_19361bins.pickle")
con_gorilla_skinhead_chaos = GorillaSkinheadChaos(
    ema_fast_length=5,
    ema_slow_length=20,
    ema_fast_source="close",
    ema_slow_source="close"
)
simulation(df, con_gorilla_skinhead_chaos)
