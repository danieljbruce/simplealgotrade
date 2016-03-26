__author__ = 'Daniel'

import ReadValue

class Position(dict):
    # Member data:
    # __portfolio = {'security 1', # of units, 'security 2', # of units, ....}
    # __time = Number of seconds since midnight on January 1st 1900.
    # __database = Database containing price information. ie. 'simplealgotrade.db'

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

    def __init__(self, pTime, pPortfolio):
        # Initialize class here.
        self.__time = pTime
        self.__portfolio = pPortfolio
        return

    def portfolio(self):
        return self.__portfolio

    def time(self):
        return self.__time

    def database(self):
        return self.__database

    def source(self):
        return self.__source

    def value(self, pSource = 0, pDatabase = 'simplealgotrade.db'):
        # Returns: The value of the position at the time given according to the given database (when sold)
        return self.__portfolio.value(self.__time, pSource, pDatabase)