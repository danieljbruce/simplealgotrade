__author__ = 'Daniel Bruce'

import sqlite3, csv

def ReadValue(pEntity, pTime, pDataBaseName = 'simplealgotrade.db', pSource = 1):
    # Returns the most recent value for the Entity pEntity before pTime
    # Test case: No results returned
    # pTime: The number of seconds since 1900 Jan 1, 00:00:00
    # pInstrument: The string matching the instrument stored in the database table
    try:
        db = sqlite3.connect(pDataBaseName)
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        # SELECT Entity, Time, Value FROM priceobservation WHERE Entity = 'EURUSD' AND Time = (SELECT MAX(Time) FROM priceobservation WHERE Time < 3630000000 AND Entity = 'EURUSD')
        sqlquery = ''' SELECT Entity, Time, Value FROM commission WHERE Entity = ? AND Time = (SELECT MAX(Time) FROM priceobservation WHERE Time < ? AND Entity = ?) '''
        sqlparameters = [pEntity, pTime, pEntity]
        cursor.execute(sqlquery, sqlparameters)
        returnValue = 0
        for row in cursor:
            returnValue = row['Value']
            continue # Just in case there is more than one row for whatever reason
        return returnValue # Exception needs to be programmed.
    except:
        print("Exception")
    #for row in cursor:
    # row['name'] returns the name column in the query, row['email'] returns email column.
    # print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))
    db.close()
