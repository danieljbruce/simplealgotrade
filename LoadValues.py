__author__ = 'Daniel'

import sqlite3, csv
import pandas

def LoadValues(pCSVFile, pDatabaseName = 'simplealgotrade.db', pSource = 0):
    # Program purge before data is entered
    conn = sqlite3.connect(pDatabaseName)
    df = pandas.read_csv(pCSVFile)
    df.to_sql('TimeSeriesData', conn, if_exists='append', index=False)
