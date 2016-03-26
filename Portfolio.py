__author__ = 'Daniel'

from copy import *
from ReadValue import *

class Portfolio(dict):
    def __init__(self, pSecurityDict):
        for k, v in pSecurityDict.items():
            self[k] = v
        return

    def value(self, pTime, pSource = 0, pDatabase = 'simplealgotrade.db'):
        # Returns the value of the portfolio given time in seconds since 00:00:00 1/1/1900 UTC.
        return 0

    def new_portfolio(self, pTrade):
        # Returns a copy of the new portfolio after a trade takes place.
        if pTrade.instrument not in self.keys():
            self[pTrade.instrument] = 0 # If the portfolio does not contain the instrument yet then set it to 0 units
        new_portfolio = copy(self)
        new_portfolio[pTrade.instrument] = new_portfolio[pTrade.instrument] + pTrade.units
        new_portfolio['__cash__'] = new_portfolio['__cash__'] - ReadValue(pTrade.instrument, pTrade.time)
        return new_portfolio