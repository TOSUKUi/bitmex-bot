import sys
sys.path.append('/mnt/c/Users/TOSUKUi/Documents/workspace/bitmex-bot')
import lib.bitmex_api_connecter as connector
from logic import vix_and_rci
from logic.conditions.vix_and_rci_condition import VixAndRciCondition

def test():
    bitmex = connector.main_connection()