import sqlite3
from CoinData import Unpack as Up


def createNewTable(tableName, exchangeName):
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()
    query = 'CREATE TABLE IF NOT EXISTS ' + tableName + '(timestamp INTEGER, open REAL, high REAL, low REAL '\
                                                        'close REAL, volume REAL) '
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()


def addOhlcv2Table(tableName, exchangeName, ohlcv):
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()
    query = 'INSERT INTO ' + tableName + ' (timestamp,open,high,low,close,volume) VALUE (?, ?, ?,?, ?,?) '
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
    if query == '':
        return
    conn = sqlite3.connect(exchangeName)
    c = conn.cursor()
    query = 'SELECT * FROM ' + tableName
    c.execute(query)
    data = c.fetchall()
    print(data)
