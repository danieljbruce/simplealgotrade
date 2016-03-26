__author__ = 'Daniel'

def LoadCommissions():
    # Fills the commissions table with the price required to buy/sell per unit and threshold cost.
    return

def LoadCommissions(pCSVFile, pDatabaseName = 'simplealgotrade.db', pSource = 0):
    # Program purge before data is entered
    conn = sqlite3.connect(pDatabaseName)
    df = pandas.read_csv(pCSVFile)
    df.to_sql('priceobservation', conn, if_exists='append', index=False)