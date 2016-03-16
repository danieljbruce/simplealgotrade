__author__ = 'Daniel'

class Position():
    # Member data:
    # __portfolio = [('security 1', # of units), ('security 2', # of units), ....]
    # __time = Number of seconds since midnight on January 1st 1900.
    # __database = Database containing price information. ie. 'simplealgotrade.db'

    def __init__(self, pTime, pPortfolio):
        # Initialize class here.
        return

    def portfolio(self):
        return self.__portfolio

    def time(self):
        return self.__time

    def database(self):
        return self.__database

    def value(self, pDatabase):
        # Returns: The value of the position at the time given according to the given database (when sold)
        return 0