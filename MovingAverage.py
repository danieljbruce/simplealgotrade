__author__ = 'Daniel'

def MovingAverage(pInstrument, pTime, pLookback, pLookbackStep, pSkipRecord = False):
    # pInstrument is the instrument that we will trade.
    # pTime is the effective time we want to calculate the moving average for.
    # pLookbackStep is the amount of time between observations.
    # pLookback is the number of steps we look back.
    # pSkipRecord tells the program to skip recording calculations in the database.
    # Example MovingAverage('EURUSD', 3630000000, 25, 60*60) is a moving average of the last 25 hours.
    # Calculations are always stored such that (storagetime - genesistime) % pLookbackStep = 0


