from CoinData import Exchanges as Ex
from CoinData import Database as Db
from CoinData import TimeConvert as Tc

# This is the file in which we will get all Binance Data.
# All this is all the pairs


FileName = 'Binance'

market = Ex.getBinanceMarket()
marketSize = len(market)

quotes = []
Pairs = dict()
for k in market:
    quote = k['quote']
    if not(quote in quotes):
        quotes.append(quote)


print(quotes)

for q in quotes:
    Pairs[q] = list()

for k in market:
    quote = k['quote']
    base = k['base']
    Pairs[quote].append(base)

for q in quotes:
    for b in Pairs[q]:
        symbol = b + '/' + q

