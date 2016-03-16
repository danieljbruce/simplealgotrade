__author__ = 'Daniel'

import sqlite3, csv
import pandas

def fLoadData(pCSVFile, pDataBaseName = 'simplealgotrade.db'):
    conn = sqlite3.connect(pDataBaseName)
    df = pandas.read_csv(pCSVFile)
    df.to_sql('priceobservation', conn, if_exists='append', index=False)