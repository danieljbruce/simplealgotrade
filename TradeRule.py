__author__ = 'Daniel'

from copy import *

class TradeRule():
    # This class generates a StrategySimulation when the 'generate' method is called.
    # This class is meant to be a base class for any trade rule that the developer wishes to construct.
    # Methods:
    # assess (Abstract): This method looks at the current position and returns the new desired portfolio position.
    # generateStrategySimulation: This method returns a StrategySimulation based on assess.

    def __init__(self, pDatabase = 'simplealgotrade.db'):
        self.database = pDatabase
        return

    def assess(self, pPortfolio, pTime):
        # Returns a trade ('security', amount - integer) ie. ('GOOG', 7) or None if no trade
        # Return value represents the action that will be taken to create the new portfolio
        # Parameters:
        # pPortfolio is a list of 2 tuples ie. [('security 1', unitsHeld), ('security 2', unitsHeld), ...]
        # pTime is the amount of time since 00:00:00 January 1st, 1900 UTC
         raise NotImplementedError

    def generate_trades(self, pStartTime, pEndTime, pTimeStep, pInitialPortfolio):
        # Begins at start time and calls assess every time step until end time in order to build a Strategy
        trades = []
        current_time = pStartTime
        current_portfolio = copy(pInitialPortfolio)
        while current_time < pEndTime:
            next_trade = self.assess(current_portfolio, current_time)
            if next_trade is not None:
                current_portfolio = current_portfolio.new_portfolio(next_trade)
                trades.append(next_trade)
            current_time += pTimeStep
        return trades

    def generate_positions(self, pStartTime, pEndTime, pTimeStep, pInitialPortfolio):
        trades = self.generate_trades(pStartTime, pEndTime, pTimeStep, pInitialPortfolio)
        self.generate_positions_from_trades(pStartTime, pEndTime, pTimeStep, pInitialPortfolio, trades)

    def generate_positions_from_trades(self, pStartTime, pEndTime, pTimeStep, pInitialPortfolio, pTrades):
        # Trades should be ordered
        positions = [(pStartTime, pInitialPortfolio)]
        current_position = pInitialPortfolio
        for i in pTrades:
            current_position = current_position.new_portfolio(i)
            positions.append((i.time, current_position))
        return positions