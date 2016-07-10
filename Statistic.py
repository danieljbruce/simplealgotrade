__author__ = 'Daniel'

class Statistic():
    # No special functionality, but meant to be seen as an interface
    def __init__(self, pName):
        self.__Name = pStartTime
        self.__EndTime = pEndTime
        self.__StartCash = pStartCash
        self.__StartPortfolio = pStartPortfolio
        self.__TradeList = pTradeList # A dictionary of string to integers combinations.
        self.__Source = pSource
        self.__Database = pDatabase
        self.__TradeList.sort() # Sort the trade list # IMPLEMENT THE COMPARISON FUNCTION.
        return

    def getValue(self, pTime):
        # This is where the logic is coded to calculate the value of the statistic.
        raise NotImplementedError

    def calculate(self, pTimeStep = None, pStartTime = None):
        # Calculates statistics as of pTime