

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