from CoinData import TimeConvert as Tc


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


# refactorOhlcv is a function used for Plots
# It takes the ohlcv and converts its timestamp to num
# and then returns the ohlcv with the different timestamp
# so it can be plotted

def refactorOhlcv(ohlcv):
    timestamp = getTimestamp(ohlcv)
    timestamp = timestamp2num(timestamp)
    openPrice = getOpen(ohlcv)
    high = getHigh(ohlcv)
    low = getLow(ohlcv)
    close = getClose(ohlcv)
    volume = getVolume(ohlcv)
    for i in range(0, len(ohlcv)):
        ohlcv[i] = timestamp[i], openPrice[i], high[i], low[i], close[i], volume[i]
    return ohlcv
