import sqlite3
import sys

def import_poloniex_candlestick_open_data(pJson, pDatabaseName = "simplealgotrade.db"):
	instrument = str(pJson[0])
	data = pJson[1]
	conn = sqlite3.connect(pDatabaseName)
	cursor = conn.cursor()
	for i in data:
		open_data = str(float(i['open']))
		date_data = str(int(i['date']))
		try:
			# # "We have {0} hectares planted to {1}.".format(49, "okra")
			delete_query = """DELETE FROM TimeSeriesData WHERE Entity='""" + instrument + """' AND Time='""" + date_data + """'"""
			insert_query = """INSERT INTO TimeSeriesData (Entity,Time,Value) VALUES ( '""" + instrument + """', '""" + date_data + """', '""" + open_data + """')"""
			print("Running SQL: ", delete_query)
			cursor.execute(delete_query)
			print("Running SQL: ", insert_query)
			cursor.execute(insert_query)
		except sqlite3.DataError:
			print("Could not import data to database.")
		except:
			print("Unexpected error:", sys.exc_info()[0])
			raise
	conn.commit()
	conn.close()