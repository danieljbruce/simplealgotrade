__author__ = 'Daniel'

import ReadValue

def MovingAverage(pInstrument, pTime = None, pLookback = 1, pLookbackStep = 60, pSkipRecord = False):
    # pInstrument is the instrument that we will trade.
    # pTime is the effective time we want to calculate the moving average for.
    # pLookbackStep is the amount of time between observations.
    # pLookback is the number of steps we look back.
    # pSkipRecord tells the program to skip recording calculations in the database.
    # Example MovingAverage('EURUSD', 3630000000, 25, 60*60)
    if pTime is None:
        print("Set pTime to now")
    pLookback = int(pLookback) # Ensures pLookback is an integer
    value = 0
    for i in range(pLookback):
        price = ReadValue(pInstrument, pTime - (i - 1) * pLookbackStep) / pLookback
        value += price
    return value