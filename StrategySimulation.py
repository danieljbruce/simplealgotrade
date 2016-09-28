__author__ = 'Daniel'

import ReadValue
import copy

class StrategySimulation():
    # Assumption: Positions change a finite number of times during the strategy lifetime
    # Member Data:
    # __Database: The database to use for your calculations.
    # __Source: The source id to use in the database for calculations.
    # __TradeList: A list of trades objects
    # __StartTime: The start time for the strategy
    # __EndTime: The end time for the strategy
    # __StartPosition: The initial position for the strategy including cash held
    # Methods:
    # show: Prints a log of what occurred during this strategy simulation.
    # show_trades:
    # broker_cost:
    # total_return: Returns the performance of the strategy (ie. -0.1 (minus 10 percent) or 0.7 (plus 70 percent) etc.)
    # sharpe_ratio: Returns the sharpe ratio for the strategy.
    # sortino_ratio: Returns the sortino ratio for the strategy.
    # annual_return: Returns the annual return for the strategy.
    # portfolios: Returns a list of the portfolio positions throughout the StrategySimulation.
    # plot: This plots the strategy on a graph.
    # __Methods__:
    # Override print function to print what happens when the strategy is executed (Instead of just printing py obj).
    # Note:
    # Commissions and Prices are stored in the sqlite3 database in tables ...

    def __init__(self, pStartTime, pEndTime, pStartCash, pStartPortfolio, pTradeList, pSource = 0, pDatabase = 'simplealgotrade.db'):
        self.__StartTime = pStartTime
        self.__EndTime = pEndTime
        self.__StartCash = pStartCash
        self.__StartPortfolio = pStartPortfolio
        self.__TradeList = pTradeList # A dictionary of string to integers combinations.
        self.__Source = pSource
        self.__Database = pDatabase
        self.__TradeList.sort() # Sort the trade list # IMPLEMENT THE COMPARISON FUNCTION.
        return

    def broker_cost(self, pTime, pTrade):
        # Returns: The cost required in cash to execute the order (Including commissions, not including purchase price).
        # Parameters:
        # pTrade is a 3-tuple (pTime, pInstrument, pUnitChange) Negative (Positive) unit change indicates a sell (Buy).
        # pTime is the time in seconds since 00:00:00 January 1st, 1900 UTC.
        # Assumptions:
        # Trade costs are assumed to be independent of the holdings in the investor portfolio. (obviously)
        # Notes:
        # This uses the commissions table in the database.
        return 0

    def portfolios(self):
        # Returns the positions given after each trade.

        it = iter(self.__TradeList) # it = iterator induced by the trade list.
        next(it) # Set 'it' to the first element.
        # Start position list accumulation
        current_portfolio = self.__StartPortfolio # Set initial portfolio
        portfolios = [] # Position list empty
        portfolios.append(current_portfolio) # Include initial position in list
        # Begin loop at first after start time and loop until we go past the end time
        while self.__StartTime >= it.time: # it[0] returns the time
            next(it)
        # Iterate through all inbetween times
        while it.time < self.__EndTime: # Exit the loop if the trade is past the end time
            cash_flow = ReadValue(it.instrument, it.time) * it.units # amount of cash to subtract from portfolio.
            commission = 0 # The commission for making the trade
            current_portfolio = copy(current_portfolio)
            current_portfolio.portfolio['__cash__'] = current_portfolio.portfolio['__cash__'] - cash_flow # Change cash in current position.
            current_portfolio[it.instrument] = current_portfolio[it.instrument] + it.units # Change the number of units held in the security for the current position.
            portfolios.append(current_portfolio)# Add that position to the list
        return portfolios # Returns a list of positions given by position object.

    def show_portfolios(self):
        portfolios = self.portfolios
        for i in portfolios:
            print(i)
        return

    def __repr__(self):
        return ''