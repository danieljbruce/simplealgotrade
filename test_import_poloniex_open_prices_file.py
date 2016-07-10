from unittest import TestCase
from FeedPoloniexCandlestickDataProcessor import import_poloniex_open_prices_file

class TestImport_poloniex_open_prices_file(TestCase):
	def test_import_poloniex_open_prices_file(self):
		import_poloniex_open_prices_file('C:\\Users\\Daniel\\Google Drive\\Programming\\Github\\Python\\simplealgotrade\\simplealgotrade\\feeds\\poloniex_feeds\\candle_stick_data\\unprocessed\\json_candlestick_data_2016_07_05_19_14_28_BTC_ETH.json')
		print("Finished test")
