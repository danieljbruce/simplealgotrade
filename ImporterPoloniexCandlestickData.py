import sqlite3
import pandas
import sys

def import_poloniex_candlestick_open_data(pJson, pDatabaseName = "simplealgotrade.db"):
	instrument = str(pJson[0])
	data = pJson[1]
	conn = sqlite3.connect(pDatabaseName)
	for i in data:
		open_data = str(float(i['open']))
		date_data = str(int(i['date']))
		try:
			# # "We have {0} hectares planted to {1}.".format(49, "okra")
			delete_query = """DELETE FROM TimeSeriesData WHERE Entity='""" + instrument + """' AND Time='""" + date_data + """'"""
			insert_query = """INSERT INTO TimeSeriesData (Entity,Time,Value) VALUES ( '""" + instrument + """', '""" + date_data + """', '""" + open_data + """')"""
			print(insert_query)
			conn.execute(delete_query)
			conn.execute(insert_query)
		except sqlite3.DataError:
			print("Could not import data to database.")
		except:
			print("Unexpected error:", sys.exc_info()[0])
			raise