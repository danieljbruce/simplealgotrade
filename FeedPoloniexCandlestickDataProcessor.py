from pprint import pprint
import json
import os
import os.path
from pathlib import Path
from ImporterPoloniexCandlestickData import import_poloniex_candlestick_open_data
from Constants import feeds_directory

def import_poloniex_open_prices():
	dir_path_source = Path(feeds_directory + '/poloniex_feeds/candle_stick_data/unprocessed')
	dir_path_target = Path(feeds_directory + '/poloniex_feeds/candle_stick_data/processed')
	working_directory = (str(os.getcwd()))
	source_directory = working_directory + str(dir_path_source)
	for i in os.listdir(source_directory):
		print(i)
		if i.endswith(".json"):
			print(i)
			import_poloniex_open_prices_file(source_directory,i)

def import_poloniex_open_prices_file(pDirectory, pFile):
	pFilePath = str(Path(pDirectory + '/' + pFile))
	with open(pFilePath) as f:
		data = json.load(f)
		import_poloniex_candlestick_open_data(data)
		print(data)

os.getcwd()