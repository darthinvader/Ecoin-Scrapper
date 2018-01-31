from CoinData import Exchanges as Ex
from CoinData import Database as Db
import ccxt

USDPairs = ['BTC', 'ETH', 'XRP', 'EOS', 'BCH', 'IOTA', 'LTC', 'NEO', 'OMG', 'ETC', 'XMR', 'DASH', 'ZEC', 'BTG',
            'ETP',
            'QTUM', 'SAN', 'SNT', 'EDO', 'YYW', 'BAT', 'AVT', 'SPK', 'RRT', 'DAT', 'TRX', 'ELF', 'ZRX', 'TNB',
            'RCN',
            'FUN', 'MNA', 'AID', 'REP', 'SNG', 'RLC']  ##,'QASH'

BTCPairs = ['ETH', 'XRP', 'EOS', 'BCH', 'IOTA', 'LTC', 'OMG', 'ETC', 'XMR', 'DASH', 'ZEC', 'BTG', 'ETP', 'QTUM',
            'SAN',
            'SNT', 'GNT', 'EDO', 'YYW', 'BAT', 'AVT', 'SPK', 'RRT', 'DAT', 'TRX', 'ELF', 'ZRX', 'TNB', 'RCN', 'FUN',
            'MNA', 'AID', 'REP', 'SNG', 'RLC']  # #,'QASH'

ETHPairs = ['EOS', 'BCH', 'IOTA', 'NEO', 'OMG', 'ETP', 'QTUM', 'SAN', 'SNT',
            'GNT', 'EDO', 'YYW', 'BAT', 'AVT', 'SPK', 'DAT', 'TRX', 'ELF', 'ZRX', 'TNB', 'RCN', 'FUN', 'MNA',
            'AID', 'REP', 'SNG', 'RLC']  ##,'QASH'

fileName = 'Bitfinex.db'


quotes = ['USD', 'BTC', 'ETH']
Pairs = dict()
Pairs['USD'] = list()
Pairs['BTC'] = list()
Pairs['ETH'] = list()


Ulen = len(USDPairs)
Blen = len(BTCPairs)
Elen = len(ETHPairs)

for i in USDPairs:
    Pairs['USD'].append(i)

for i in BTCPairs:
    Pairs['BTC'].append(i)

for i in ETHPairs:
    Pairs['ETH'].append(i)

for q in quotes:
    for b in Pairs[q]:
        tableName = b + q
        symbol = b + '/' + q
        Db.createNewTable(tableName, fileName)
        timestamp = Db.getMaxTimestamp(tableName, fileName)
        if timestamp is None:
            Ex.DbMake(exchange=ccxt.bitfinex2(), symbol=symbol, timeframe='1m', fileName=fileName,waiting=3)
        else:
            Ex.DbMake(exchange=ccxt.bitfinex2(), symbol=symbol, timeframe='1m', startTimestamp=timestamp * 1000
                      , fileName=fileName, waiting=3)

