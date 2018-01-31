from CoinData import Exchanges as Ex
from CoinData import Database as Db
from CoinData import TimeConvert as Tc
import ccxt

# This is the file in which we will get all Binance Data.

fileName = 'Binance.db'

market = Ex.getBinanceMarket()
marketSize = len(market)

#We firstly get all the quotes

quotes = []
Pairs = dict()
for k in market:
    quote = k['quote']
    if not(quote in quotes):
        quotes.append(quote)

for q in quotes:
    Pairs[q] = list()

# Then we take all the different markers
for k in market:
    quote = k['quote']
    base = k['base']
    Pairs[quote].append(base)

# For each quote and for each market we go and take the data that we don't have

for q in quotes:
    for b in Pairs[q]:
        tableName = b+q
        symbol = b + '/' + q
        Db.createNewTable(tableName, fileName)
        timestamp = Db.getMaxTimestamp(tableName, fileName)
        if timestamp is None:
            Ex.DbMake(exchange=ccxt.binance(), symbol=symbol, timeframe='1m', fileName=fileName)
        else:
            Ex.DbMake(exchange=ccxt.binance(), symbol=symbol, timeframe='1m', startTimestamp=timestamp*1000
                      , fileName=fileName)