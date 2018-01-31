import sqlite3
from CoinData import Unpack as Up
from CoinData import TimeConvert as Tc


def createNewTable(tableName, exchangeName):
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()

    query = 'CREATE TABLE IF NOT EXISTS ' + tableName + '(timestamp INTEGER, open REAL, ' \
                                                        'high REAL, low REAL, close REAL, volume REAL)'
    c.execute(query)
    conn.commit()

    c.close()
    conn.close()


def addOhlcv2Table(tableName, exchangeName, ohlcv):
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()

    query = 'INSERT INTO ' + tableName + ' (timestamp, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?)'

    size = len(ohlcv)

    timestamp = Up.getTimestamp(ohlcv)
    openp = Up.getOpen(ohlcv)
    high = Up.getHigh(ohlcv)
    low = Up.getLow(ohlcv)
    close = Up.getClose(ohlcv)
    volume = Up.getVolume(ohlcv)

    for i in range(0, size):
        c.execute(query, (timestamp[i], openp[i], high[i], low[i], close[i], volume[i]))
    conn.commit()

    c.close()
    conn.close()


def getTable2Ohlcv(tableName, exchangeName, query=''):
    if query != '':
        return

    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()

    query = 'SELECT * FROM ' + tableName
    c.execute(query)

    data = c.fetchall()
    ohlcv = tuple2Ohlcv(data)

    c.close()
    conn.close()

    return ohlcv


def addOhlcv2Table2(tableName, exchangeName, ohlcv):
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()

    data = ohlcv2Tuples(ohlcv)

    query = 'INSERT INTO ' + tableName + ' (timestamp, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?)'
    c.executemany(query, data)
    conn.commit()

    c.close()
    conn.close()


# ohclvForDatabase
# takes the ohlcv and transforms its timestamp to the Unix Epoch
# so the integer is smaller (normal timestamp is unix Epoch*1000)
# this became obsolete because every ohlcv will be returned with normal epochs


def ohclvForDatabase(ohlcv):
    timestamp = Up.getTimestamp(ohlcv)
    timestamp = Tc.timestamp2UnixEpoch(timestamp)

    size = len(ohlcv)
    for i in range(0, size):
        ohlcv[i][0] = timestamp[i]
    return ohlcv


def getMaxTimestamp(tableName,exchangeName):
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()

    query = 'SELECT MAX(timestamp) FROM ' + tableName
    c.execute(query)

    data = c.fetchall()
    return data

# ohlcv2Tuples
# input an ohlcv and converts it to ohlcv but instead of list it makes it tuples


def ohlcv2Tuples(ohlcv):
    tuples = [tuple(l) for l in ohlcv]
    return tuples

# tupleOhlcv2Ohlcv
# take a tuple ohlcv (a list of tuples)
# and converts its into an original ohlcv (a list of lists)
# this works when pulling data from the database instead of the sites


def tuple2Ohlcv(data):
    k = [list(x) for x in data]
    return k
