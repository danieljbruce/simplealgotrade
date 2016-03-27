__author__ = 'Daniel'

from TradeRule import *
from ReadValue import *
from Trade import *

class TradeRule_WeekBuy(TradeRule):
    def assess(self, pPortfolio, pTime):
        # This trade rule takes a long position in 'EURUSD' at midnight the first 2 days of every 7 days
        # This trade rule exits this position at midnight at the end of the 2nd day
        print("Assessing at time:", str(pTime))
        if 'EURUSD' not in pPortfolio.keys():
            pPortfolio['EURUSD'] = 0
        if pTime % (60*60*24*7) <= 60*60*24*2 and pPortfolio['EURUSD'] == 0: # If statement to enter long position.
            print('Buy EURUSD at price ', ReadValue('EURUSD', pTime))
            if ReadValue('EURUSD', pTime) != 0:
                self.units = int(pPortfolio['__cash__'] / ReadValue('EURUSD', pTime))
                return Trade(pTime, 'EURUSD', self.units)
        if pTime % (60*60*24*7) >= 60*60*24*2 and pPortfolio['EURUSD'] != 0: # If statement to exit long position.
            print('Sell EURUSD at price ', ReadValue('EURUSD', pTime))
            return Trade(pTime, 'EURUSD', -self.units)
            self.units = 0
        return None # No trade is made