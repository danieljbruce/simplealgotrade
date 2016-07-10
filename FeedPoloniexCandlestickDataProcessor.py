from pprint import pprint
import json
import os
from ImporterPoloniexCandlestickData import import_poloniex_candlestick_open_data

def import_poloniex_open_prices():
	source = '\\'+'\\'
	target = '\\'
	working_directory = str(os.getcwd()).replace(source,  target)
	target_directory = working_directory + r'\feeds\poloniex_feeds\candle_stick_data\unprocessed'
	for i in os.listdir(target_directory):
		if i.endswith(".json"):
			import_poloniex_open_prices_file(target_directory,i)

def import_poloniex_open_prices_file(pDirectory, pFile):
	pFilePath = pDirectory + "\\" + pFile
	with open(pFilePath) as f:
		data = json.load(f)
		import_poloniex_candlestick_open_data(data)
		print(data)

os.getcwd()