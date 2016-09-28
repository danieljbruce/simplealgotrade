from copy import copy;
import asyncio;
import requests;
import time;
import datetime;
import threading;

def get_url_from_url_mask(pUrlMask, pInstrument, pPeriod, pStartTime, pEndTime):
    # Returns a Url containing no {} characters.
    returnValue = copy.copy(pUrlMask);
    returnValue = returnValue.replace('{instrument}', pInstrument);
    returnValue = returnValue.replace('{start}', pStartTime)
    returnValue = returnValue.replace('{end}', pEndTime)
    returnValue = returnValue.replace('{period}', pPeriod)
    return returnValue;

def download_candlestick_data_with_url_mask(pUrlMask, pInstrument, pPeriod, pStartTime, pEndTime):
    # Takes pUrlMask and downloads json files into the 'feeds' folder.
    # Valid currency pairs include BTC_ETH, ....
    # Time is number of seconds since .....
    # Returns: json of the desired chart data.
    strRequestTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
    strUrl = get_url_from_url_mask(pUrlMask, pInstrument, pPeriod, pStartTime, pEndTime);
    response = requests.get(strUrl, verify=True);  # Verify is check SSL certificate
    strResponseTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
    jsonData = response.json();
    #Consider adding 'batchsize' to header
    jsonFileContents = {'header': {'request_time': strRequestTime, 'response_time' : strResponseTime, 'url_request': strUrl, 'instrument':pInstrument}, 'data':jsonData};

def download_candlestick_data_using_candlestick_entity_table():
    # Use: http: // stackoverflow.com / questions / 22190403 / how - could - i - use - requests - in -asyncio
    loop = asyncio.get_event_loop();
    # Get CandlestickEntity table joined with the CandlestickSource table as json
    # Loop through the CandlestickEntity table joined with the candlestick source table:
    # SELECT * FROM CandlestickEntity cse INNER JOIN CandleStickSource css ON cse.SourceID = css.sourceID;
        # Using the JSON with the help of the CandlestickSource table, download a file from the exchange's API.
        # Maybe break the json files into chunks
        # Create a list of threads
    return;