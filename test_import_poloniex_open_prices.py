from unittest import TestCase
from FeedPoloniexCandlestickDataProcessor import import_poloniex_open_prices

class TestImport_poloniex_open_prices(TestCase):
	def test_import_poloniex_open_prices(self):
		import_poloniex_open_prices()
