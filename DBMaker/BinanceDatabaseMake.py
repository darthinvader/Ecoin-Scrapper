from CoinData import Exchanges as Ex
from CoinData import Database as Db
# This is the file in which we will get all Binance Data.
# All this is all the pairs
USDTPairs = ['BTC','ETH','NEO','BNB','LTC','BCH']

BTCPairs = ['ETH','ICX','IOST','TRX','XRP','ELF','NEO','WTC','BNB','CMT','VEN','EOS','VIB','MTH','HSR','XLM','LTC','ADA','CND','ETC','POE','GAS',
            'BRD','IOTA','LUN','BCH','LEND','OMG','QTUM','XVG','AION','BTS','DASH','PPT','GVT','ICN','RCN','VIBE','GTO','XMR','ZRX','ENJ','STRAT',
            'APPC','ARN','SUB','KNC','MTL','ADX','AMB','WABI','TNT','LSK','WINGS','TNB','SNT','SNM','AST','INS','ENG','LRC','NEBL','CDT','OST',
            'MDA','LINK','QSP','BTG','BCD','YOYO','BAT','KMD','RDN','REQ','SALT','BQX','OAX','FUN','ZEC','XZC','POWR','MANA','BCPT','CTR','TRIG',
            'FUEL','PIVX','NULS','MOD','EDO','SNGLS','ARK','EVX','BNT','WAVES','NAV','DGD','MCO','RLC','DNT','STORJ','GXS','DLT',]

ETHPairs = ['TRX','ICX','XRP','NEO','EOS','VEN','WTC','IOST','ELF','CMT','XLM','VIB','ADA','MTH','BNB','LTC','CND','IOTA','OMG','BCH','POE','PPT',
            'LEND','ETC','ZRX','QTUM','XVG','BTS','AION','LUN','HSR','REQ','KNC','APPC','RDN','ICN','LRC','SUB','QSP','AMB','XMR','GVT','ADX','OST',
            'ENJ','WABI','LINK','SNT','AST','VIBE','RCN','TNT','INS','ENG','TNB','DASH','ARN','SNM','FUN','CDT','POWR','NULS','YOYO','GTO','LSK',
            'SALT','BAT','STRAT','BQX','NEBL','BRD','CTR','OAX','FUEL','MOD','BNT','KMD','XZC','SNGLS','BCPT','BCD','BTG','MANA','GXS','ARK','ZEC',
            'MDA','WAVES','PIVX','EVX','DGD','DNT','RLC','TRIG','EDO','DLT','MCO','NAV','MTL','STORJ','WINGS']

BNBPairs = ['ICX','NEO','VEN','CMT','ADX','WTC','CND','XLM','LTC','IOTA','BCH','BTS','QSP','APPC','AION','AMB','NEBL','GTO','NULS','YOYO','POWR',
            'LSK','WABI','BAT','OST','RDN','PIVX','BCPT','BRD','XZC','TRIG','DLT','NAV','RLC','WAVES','MCO']


FileName = 'Binance'
USDTsize = len(USDTPairs)
BTCsize = len(BTCPairs)
ETHsize = len(ETHPairs)
BNBsize = len(BNBPairs)

USDTpostfix = 'USDT'
BTCpostfix = 'BTC'
ETHpostfix = 'ETH'
BNBpostfix = 'BNB'



