from unittest import TestCase
from PoloniexAPI import PoloniexAPI
import json
from datetime import datetime

class TestPoloniexAPI(TestCase):
	def test_fetch_chart_data_1(self):
		timestamp = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
		api = PoloniexAPI("","")
		json_data = api.fetch_candlestick_data("BTC_ETH", 1465699200, 1465704000, 300)
		with open('feeds/poloniex_feeds/candle_stick_data/unprocessed/json_candlestick_data_' + timestamp + '_BTC_ETH.json', 'w') as outfile:
			json.dump(json_data, outfile)