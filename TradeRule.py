__author__ = 'Daniel'

class TradeRule():
    # This class generates a StrategySimulation when the 'generate' method is called.
    # This class is meant to be a base class for any trade rule that the developer wishes to construct.
    # Methods:
    # assess (Abstract): This method looks at the current position and returns the new desired portfolio position.
    # generateStrategySimulation: This method returns a StrategySimulation based on assess.

    def __init__(self, pDatabase):
        self.database = pDatabase
        return

    def assess(self, pCash, pTime, pSecurityList):
        # Returns a security list ie. [('security 1', unitsHeld), ('security 2', unitsHeld), ...]
        # Return value represents the new position for the portfolio
        # Parameters:
        # pSecurity list is a list of 2 tuples ie. [('security 1', unitsHeld), ('security 2', unitsHeld), ...]
        # pTime is the amount of time since 00:00:00 January 1st, 1900 UTC
         raise NotImplementedError

    def generateStrategySimulation(self, pStartTime, pEndTime, pTimeStep, pInitialCash, pInitialSecurityList):
        # Begins at start time and calls assess every time step until end time in order to build a Stra
