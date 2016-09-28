__author__ = 'Daniel'

from copy import *
from ReadValue import *

class Portfolio(dict):
    def __init__(self, pSecurityDict):
        for k, v in pSecurityDict.items():
            self[k] = v
        return

    def value(self, pTime, pSource = 0, pDatabase = '/web-interface/simplealgotrade.db'):
        # Returns the value of the portfolio given time in seconds since 00:00:00 1/1/1900 UTC.
        value = 0
        for k, v in self.items():
            if k != '__cash__':
                value += (ReadValue(k, pTime, pSource, pDatabase) * v)
            else:
                value += v
        return value

    def new_portfolio(self, pTrade):
        # Returns a copy of the new portfolio after a trade takes place.
        if pTrade.instrument not in self.keys():
            self[pTrade.instrument] = 0 # If the portfolio does not contain the instrument yet then set it to 0 units
        new_portfolio = copy(self)
        new_portfolio[pTrade.instrument] = new_portfolio[pTrade.instrument] + pTrade.units
        new_portfolio['__cash__'] = new_portfolio['__cash__'] - ReadValue(pTrade.instrument, pTrade.time) * pTrade.units
        return new_portfolio

    # Dictionary Overrides
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return self.__dict__.has_key(k)

    def pop(self, k, d=None):
        return self.__dict__.pop(k, d)

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict):
        return cmp(self.__dict__, dict)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))