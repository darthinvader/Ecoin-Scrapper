import ccxt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc
from datetime import datetime
import time


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


# getTimestamp
# Arguments:
# ohlcv containing the arrays of screenshots of data
# returns: an array containing timestamps for each screenshot


def getTimestamp(ohlcv):
    timestamp = [x[0] for x in ohlcv]
    return timestamp


# getOpen
# Arguments:
# ohlcv containing the arrays of screenshots of data
# returns: an array containing the open prices for each screenshot


def getOpen(ohlcv):
    openPrice = [x[1] for x in ohlcv]
    return openPrice


# getHigh
# Arguments:
# ohlcv containing the arrays of screenshots of data
# returns: an array containing the high prices for each screenshot


def getHigh(ohlcv):
    high = [x[2] for x in ohlcv]
    return high


# getLow
# Arguments:
# ohlcv containing the arrays of screenshots of data
# returns: an array containing the high prices for each screenshot


def getLow(ohlcv):
    low = [x[3] for x in ohlcv]
    return low


# getClose
# Arguments:
# ohlcv containing the arrays of screenshots of data
# returns: an array containing the close prices for each screenshot


def getClose(ohlcv):
    close = [x[4] for x in ohlcv]
    return close


# getVolume
# Arguments:
# ohlcv containing the arrays of screenshots of data
# returns: an array containing the volume for each screenshot


def getVolume(ohlcv):
    volume = [x[5] for x in ohlcv]
    return volume


# timestampToDate
# Arguments:
# ohlcv:containing the arrays of screenshots of data
# return the timestamps in the format of Year-Month-Day Hour-Minute-Seconds


def timestampToDate(timestamp):
    dates = [datetime.fromtimestamp(int(str(x)[:-3])).strftime('%Y-%m-%d %H:%M:%S') for x in timestamp]
    return dates


# dateToTimestamp
# Arguments:
# date containing a single datetime
# return the timestamps in the format of Year-Month-Day Hour-Minute-Seconds
# will probably be removed(TOBEREMOVED)


def dateToTimestamps(date):
    timestamp = time.mktime(datetime.strptime(date, '%Y-%m-%d %H:%M:%S').timetuple())
    print(timestamp)
    timestamp = int(timestamp * 1000)

    return timestamp


def timestampToUnixEpoch(timestamp):
    timestamp = [int(str(x)[:-3]) for x in timestamp]
    return timestamp


# __timestamp2num
# Takes the timestamps and converts it to num and then returns it

def __timestamp2num(timestamp):
    timestamp = timestampToUnixEpoch(timestamp)
    timestamp = mdates.epoch2num(timestamp)
    return timestamp


# __newOhlcv is a function used for candlstickPlot
# not to be used from outside
# It takes the ohlcv and converts its timestamp to num
# and then returns the ohlcv with different the different timestamp


def __newOhlcv(ohlcv):
    timestamp = getTimestamp(ohlcv)
    timestamp = __timestamp2num(timestamp)
    openPrice = getOpen(ohlcv)
    high = getHigh(ohlcv)
    low = getLow(ohlcv)
    close = getClose(ohlcv)
    volume = getVolume(ohlcv)
    for i in range(0, len(ohlcv)):
        ohlcv[i] = timestamp[i], openPrice[i], high[i], low[i], close[i], volume[i]
    return ohlcv


# formatMake is a function used for Plots
# not to be used from outside
# it takes the timestamp and returns the format in which the date is shown


def __formatMake(timestamp):
    timestamp = timestampToUnixEpoch(timestamp)
    timeframes = len(timestamp)
    timedif = timestamp[2] - timestamp[1]
    timeline = timedif * timeframes
    if timeline <= 86400:  # 1440 = 24 hours * 60 minutes *60 seconds
        dateFormat = '%H:%M'
    elif timeline <= 2592000:  # 43200 = 30 days *24 hours *60 minutes *60 seconds
        dateFormat = '%dd %Hh'
    elif timeline <= 31104000:  # 518400 = 12 * 30 days *24 hours *60 minutes *60seconds
        dateFormat = '%m-%d'
    else:
        dateFormat = '%Y-%m-%d'
    return dateFormat


# candlestickPlot
# Arguments:
# ohcvl containing the arrays of screenshots of data
# the title of the candlestick chart
# this function shows a candlestick chart of the data you gave (must be in ohlcv order)

def candlestickPlot(ohlcv, title="stock"):
    if len(ohlcv) <= 2:
        print("length of data is less that 3")
        return
    timestamp = getTimestamp(ohlcv)
    dateFormat = __formatMake(timestamp)
    title += " begins:" + timestampToDate(timestamp)[0]
    timestamp = timestampToUnixEpoch(timestamp)

    widthMul = (timestamp[2] - timestamp[1]) / 60
    ohlcv = __newOhlcv(ohlcv)
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    width = (widthMul * 0.005) / (len(ohlcv) + 5)
    candlestick_ohlc(ax1, ohlcv, width=width, colorup='#00FF00', colordown='#FF0000')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter(dateFormat))
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(title)
    plt.show()


# timeClosePlot
# Arguments:
# ohlcv:containing the arrays of screenshots of data
# The function shows a normal plot of the close price relative to time


def timeDataPlot(timestamp, data):
    dateFormat = __formatMake(timestamp)
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    timestamp = __timestamp2num(timestamp)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter(dateFormat))
    ax1.plot(timestamp, data)
    plt.show()
