__author__ = 'Daniel Bruce'

class BacktestingStrategy():
    # Assumption: Positions change a finite number of times during the strategy lifetime
    # Member Data:
    # __PositionList: A list of positions
    # __StartTime: The start time for the strategy
    # __EndTime: The end time for the strategy
    # __StartCash: The initial capital for the strategy
    # Methods:
    # totalReturn: Returns the performance of the strategy (ie. -0.1 (minus 10 percent) or 0.7 (plus 70 percent) etc.)
    # sharpeRatio: Returns the sharpe ratio for the strategy.
    # sortinoRatio: Returns the sortino ratio for the strategy.
    # annualReturn: Returns the annual return for the strategy.
    # plot: This plots the strategy on a graph.
    # Note:
    # Commissions and Prices are stored in the sqlite3 database in tables ...

    #def testStrategy


    # This object stores the positions in the form of a sorted list of pairs containing: ['security 1', # of units]