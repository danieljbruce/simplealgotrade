from unittest import TestCase
from PoloniexAPI import PoloniexAPI
import json
import time

class TestPoloniexAPI(TestCase):
	def test_fetch_chart_data_1(self):
		api = PoloniexAPI("","")
		json_data = api.fetch_chart_data("BTC_ETH", 1465699200, 1465704000, 300)
		#print(json)
		current_date = time.strftime("%Y_%m_%d_%H_%M_%S")
		with open('feeds/poloniex_feeds/candle_stick_data/unprocessed/json_price_data_' + current_date + '.json', 'w') as outfile:
			json.dump(json_data, outfile)