import urllib, json
import urllib.request
import requests

class PoloniexAPI:
	def __init__(self, APIKey, Secret):
		self.APIKey = APIKey
		self.Secret = Secret

	def fetch_chart_data(self, pPair = "BTC_ETH", pStart = 0, pEnd = 9999999999, pPeriod = 300):
		# Valid currency pairs include BTC_ETH, ....
		# Time is number of seconds since .....
		# Returns: json of the desired chart data.
		strPeriod = str(pPeriod)
		strEnd = str(pEnd)
		strStart = str(pStart)
		# Try in Browser: "https://poloniex.com/public?command=returnChartData&currencyPair=BTC_ETH&start=0&end=9999999999&period=300"
		strUrl = "https://poloniex.com/public?command=returnChartData&currencyPair="+pPair+"&start="+strStart+"&end="+strEnd+"&period="+strPeriod
		response = requests.get(strUrl, verify=True)  # Verify is check SSL certificate
		data = response.json()
		return [pPair, data]

	def get_historical_data(self, pPair, pStart, pEnd, pPeriod):
		return