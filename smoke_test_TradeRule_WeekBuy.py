__author__ = 'Daniel'

from TradeRule_WeekBuy import TradeRule_WeekBuy
from Portfolio import *

rule = TradeRule_WeekBuy()
start_time = 60*60*24*365*115 + 60*60*24*40
end_time = 60*60*24*365*115 + 60*60*24*340
time_step = 60*60
start_portfolio = Portfolio({'__cash__': 2000, 'EURUSD' : 0}) # Numeraire is __cash__ (USD assumed)
trades = rule.generate_trades(start_time, end_time, time_step, start_portfolio)
positions = rule.generate_positions_from_trades(start_time, end_time, time_step, start_portfolio, trades)
print(trades)
print(positions)