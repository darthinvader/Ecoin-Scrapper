import ccxt
from CoinData import TimeConvert as Tc
from CoinData import Unpack as Up
from CoinData import Database as Db
import time

timeJump = [60, 180, 300, 900, 1800, 3600, 7200, 14400, 21600, 28800, 43200, 86400, 259200, 604800, 2592000]
timing = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']


def getOhlcv(exchange=ccxt.binance(), symbol='BTC/USDT', timeframe='1m', since=None, limit=500):
    ohlcv = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, since=since, limit=limit)

    timestamp = Up.getTimestamp(ohlcv)
    timestamp = Tc.timestamp2UnixEpoch(timestamp)

    size = len(ohlcv)
    for i in range(0, size):
        ohlcv[i][0] = timestamp[i]
    return ohlcv

# getBInanceStartingDate
# Arguments:
# Symbol: "Coin/Coin or Fiat Currency" e.g "BTC/USDT","ETH/BTC" default:"BTC/USDT"
# returns the Date which the data first appeared in Binance


def getStartingDate(exchange=ccxt.binance(), symbol='BTC/USDT'):
    date1 = '2000-01-01 00:00:00'
    timestamp = Tc.date2Timestamp(date1)
    ohlcv = getOhlcv(exchange, since=timestamp, symbol=symbol, limit=1)
    startDate = ohlcv[0][0] * 1000
    return startDate

# advanceTimestamp
# Arguments:
# currDate: the date we have right now
# timeframe: the ammount of time passed between each screenshot
# returns the Date which the data first appeared in Binance


def advanceTimestamp(lastDate, timeframe='1m',):
    if timeframe in timing:
        index = timing.index(timeframe)
        print(index)
        print(lastDate)
        timestamp = (lastDate + timeJump[index])*1000
        return timestamp
    else:
        print("error")

# getAllData
# returns a huge ohlcv from the startTime to the now


def getAllData(exchange=ccxt.binance(), symbol='BTC/USDT', timeframe='1m', startTimestamp='', waiting=0):
    if startTimestamp == '':
        startTimestamp = getStartingDate(exchange, symbol)
        print("it is null")
    currTimestamp = startTimestamp
    print(currTimestamp)
    ohlcv = []

    flag = True

    while flag:
        currOhlcv = getOhlcv(exchange, symbol=symbol, since=currTimestamp, timeframe=timeframe, limit=500)
        ohlcv.extend(currOhlcv)
        if len(currOhlcv) < 500:
            print('what?')
            break
        currTimestamp = advanceTimestamp(currOhlcv[499][0], timeframe=timeframe)
        time.sleep(waiting)
    return ohlcv


# getBinanceOhlcv
# Arguments:
# Symbol: "Coin/Coin or Fiat Currency" e.g "BTC/USDT","ETH/BTC" default:"BTC/USDT"
# timeframe: the amount of time passed between each screenshot of data e.g"1m","1h" default:"1m"
# since: the data begin in the time specified in unix format
# default:None will return data from the current time-(limit*timeframe)
# limit:the amount of screenshots of data you get e.g 50 default:500 max:500
# returns:an array containing each screenshot of data at the specified timestamp
# Each screenshot contains [Timestamp,Open,High,Low,Close,Volume]


def getBinanceOhlcv(symbol='BTC/USDT', timeframe='1m', since=None, limit=500):
    ohlcv = getOhlcv(ccxt.binance(), symbol, timeframe, since, limit)
    return ohlcv

# BinanceData
# Arguments:
# Symbol: "Coin/Coin or Fiat Currency" e.g "BTC/USDT","ETH/BTC" default:"BTC/USDT"
# timeframe: the amount of time passed between each screenshot of data e.g"1m","1h" default:"1m"
# returns all the Data from the beginning till now of the selected coin in the selected timeframe
# in a ohlcv data


def BinanceData(symbol='BTC/USDT', timeframe='1m', startTimestamp=''):
    ohlcv = getAllData(ccxt.binance(), symbol, timeframe, startTimestamp,0)
    return ohlcv

# getBinanceMarket
# returns all the different markets of binance


def getBinanceMarket():
    exchange = ccxt.binance()
    t = exchange.fetch_markets()
    return t


# getBitmexOhlcv
# Arguments:
# Symbol: "Coin/Coin or Fiat Currency" e.g "BTC/USDT","ETH/BTC" default:"BTC/USDT"
# timeframe: the amount of time passed between each screenshot of data e.g"1m","1h" default:"1m"
# since: the data begin in the time specified in unix format
# default:None will return data from the current time-(limit*timeframe)
# limit:the amount of screenshots of data you get e.g 50 default:500 max:500
# returns:an array containing each screenshot of data at the specified timestamp
# Each screenshot contains [Timestamp,Open,High,Low,Close,Volume]


def getBitfinexOhlcv(symbol='BTC/USD', timeframe='1m', since=None, limit=500):
    ohlcv = getOhlcv(ccxt.bitfinex2(), symbol, timeframe, since, limit)
    return ohlcv

# BitfinexData
# Arguments:
# Symbol: "Coin/Coin or Fiat Currency" e.g "BTC/USDT","ETH/BTC" default:"BTC/USDT"
# startTimestamp is the time where you want to start getting data
# timeframe: the amount of time passed between each screenshot of data e.g"1m","1h" default:"1m"
# returns all the Data from the beginning till now of the selected coin in the selected timeframe
# in a ohlcv data


def BifinexData(symbol='BTC/USD', timeframe='1m', startTimestamp=''):
    ohlcv = getAllData(ccxt.bitfinex2(), symbol, timeframe, startTimestamp, 3)
    return ohlcv


def DbMake(exchange=ccxt.binance(), symbol='BTC/USDT', timeframe='1m', startTimestamp='', waiting=0, fileName='Binance.db'):
    tableName = symbol.replace('/', '', 1)

    if startTimestamp == '':
        startTimestamp = getStartingDate(exchange, symbol)
        print("it is null")
    currTimestamp = startTimestamp

    print(currTimestamp)

    flag = True

    while flag:
        ohlcv = getOhlcv(exchange, symbol=symbol, since=currTimestamp, timeframe=timeframe, limit=500)
        if len(ohlcv) < 500:
            print('what?')
            break
        Db.addOhlcv2Table2(tableName, fileName, ohlcv)
        currTimestamp = advanceTimestamp(ohlcv[499][0], timeframe=timeframe)
        time.sleep(waiting)
    ohlcv[:-1]
    if len(ohlcv != 0):
        Db.addOhlcv2Table2(tableName, fileName, ohlcv)
