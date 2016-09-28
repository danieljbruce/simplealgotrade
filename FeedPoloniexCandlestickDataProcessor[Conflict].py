from pprint import pprint
import json
import os
import shutil
from ImporterPoloniexCandlestickData import import_poloniex_candlestick_open_data

def import_poloniex_open_prices():
	source = '\\'+'\\'
	target = '\\'
	working_directory = str(os.getcwd()).replace(source,  target)
	target_directory = working_directory + r'\poloniex_feeds\candle_stick_data\unprocessed'
	destination_directory = working_directory + r'\feeds\poloniex_feeds\candle_stick_data\processed'
	for i in os.listdir(target_directory):
		if i.endswith(".json"):
			try:
				import_poloniex_open_prices_file(target_directory,i)
			except:
				print("Error importing files.")
			try:
				shutil.move(target_directory + "\\" + i, destination_directory + "\\" + i)
			except:
				print("Error moving files.")

def import_poloniex_open_prices_file(pDirectory, pFile):
	pFilePath = pDirectory + "\\" + pFile
	with open(pFilePath) as f:
		data = json.load(f)
		import_poloniex_candlestick_open_data(data)
		print("Imported data: ", data)

os.getcwd()