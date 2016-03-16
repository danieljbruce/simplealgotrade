__author__ = 'Daniel'

class StrategySimulation():
    # Assumption: Positions change a finite number of times during the strategy lifetime
    # Member Data:
    # __Database: The database to use for your calculations.
    # __Source: The source id to use in the database for calculations.
    # __TradeList: A list of trades ie. [(time1, instrument1, unitchange1), (time2, instrument2, unitchange2), ...]
    # __StartTime: The start time for the strategy
    # __EndTime: The end time for the strategy
    # __StartCash: The initial capital for the strategy
    # __StartPosition: The initial position for the strategy
    # Methods:
    # totalReturn: Returns the performance of the strategy (ie. -0.1 (minus 10 percent) or 0.7 (plus 70 percent) etc.)
    # sharpeRatio: Returns the sharpe ratio for the strategy.
    # sortinoRatio: Returns the sortino ratio for the strategy.
    # annualReturn: Returns the annual return for the strategy.
    # positionList: Returns a list of the portfolio positions throughout the StrategySimulation.
    # plot: This plots the strategy on a graph.
    # __Methods__:
    # Override print function to print what happens when the strategy is executed (Instead of just printing py obj).
    # Note:
    # Commissions and Prices are stored in the sqlite3 database in tables ...

    def __init__(self, pStartTime, pEndTime, pStartCash, pStartPosition, pPositionList):
        return

    def brokerCost(self, pTime, pTrade):
        # Returns: The cost required in cash to execute the order (Including commissions, not including purchase price).
        # Parameters:
        # pTrade is a 3-tuple (pTime, pInstrument, pUnitChange) Negative (Positive) unit change indicates a sell (Buy).
        # pTime is the time in seconds since 00:00:00 January 1st, 1900 UTC.
        # Assumptions:
        # Trade costs are assumed to be independent of the holdings in the investor portfolio. (obviously)
        # Notes:
        # This uses the commissions table in the database.

    #def testStrategy


    # This object stores the positions in the form of a sorted list of pairs containing: ['security 1', # of units]
