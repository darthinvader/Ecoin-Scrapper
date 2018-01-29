import ccxt
from CoinData import TimeConvert as Tc

timeJump = [60, 180, 300, 900, 1800, 3600, 7200, 14400, 21600, 28800, 43200, 86400, 259200, 604800, 2592000]
timing = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']


# getOhlcv
# Arguments:
# Symbol: "Coin/Coin or Fiat Currency" e.g "BTC/USDT","ETH/BTC" default:"BTC/USDT"
# timeframe: the amount of time passed between each screenshot of data e.g"1m","1h" default:"1m"
# since: the data begin in the time specified in unix format
# default:None will return data from the current time-(limit*timeframe)
# limit:the amount of screenshots of data you get e.g 50 default:500 max:500
# returns:an array containing each screenshot of data at the specified timestamp
# Each screenshot contains [Timestamp,Open,High,Low,Close,Volume]


def getOhlcv(symbol='BTC/USDT', timeframe='1m', since=None, limit=500):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    return ohlcv


def getStartingDate(symbol='BTC/USDT'):
    date1 = '2017-01-01 00:00:00'
    timestamp = Tc.date2Timestamp(date1)
    since = timestamp
    ohlcv = getOhlcv(since=since, symbol=symbol, limit=1)
    startDate = ohlcv[0][0]
    return startDate


def __advanceTimestamp(currDate, timeframe='1m'):
    multiplier = 1000
    if timeframe in timing:
        index = timing.index(timeframe)
        timestamp = currDate + timeJump[index] * multiplier * 500
        return timestamp
    else:
        print("error")


def BinanceData(symbol='BTC/USDT', timeframe='1m'):
    startTimestamp = getStartingDate(symbol)
    currTimestamp = startTimestamp
    ohlcv = []
    flag = True
    while flag:
        currOhlcv = getOhlcv(symbol=symbol, since=currTimestamp, timeframe=timeframe)
        ohlcv.extend(currOhlcv)
        currTimestamp = __advanceTimestamp(currTimestamp, timeframe=timeframe)
        print(currTimestamp)
        if len(currOhlcv) < 500:
            flag = False
    return ohlcv