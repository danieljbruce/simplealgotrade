__author__ = 'Daniel'

from pandas import *
from sqlite3 import *

def LoadCommissions():
    # Fills the commissions table with the price required to buy/sell per unit and threshold cost.
    return

def LoadCommissions(pCSVFile, pSource = 0, pDatabaseName = 'simplealgotrade.db'):
    # Program purge before data is entered
    conn = sqlite3.connect(pDatabaseName)
    df = pandas.read_csv(pCSVFile)
    df.to_sql('priceobservation', conn, if_exists='append', index=False)