from CoinData import TimeConvert as Tc
from CoinData import Exchanges as Ex
from CoinData import Plots as Pl
from CoinData import Unpack as Up


def binanceCandlePlot():

    # Here we show how to take data from binance

    # There are many different exchange pairs to be used for example the one below
    symbol = 'ETH/BTC'

    # There are also many timeframes that show the time between every candlestick
    timeframe = '1d'

    # There is also the time we want the data to start
    startDate = '2017-12-23 00:00:00'

    # Then we make the date into binance Timestamp(Unix epoch +3 0s at the end)
    since = Tc.date2Timestamps(startDate)

    # Then we specify the ammount of data we want(max 500 min 2)

    limit = 40
    ohlcv = Ex.getBinanceOhlcv(symbol, timeframe, since, limit)
    # All the data in ohlcv have default values that can be used(check CoinData/Exchanges.py)

    # Now that we have ohlcv we can use it
    # ohlcv stands for (open high low close volume)
    # It also contains a timestamp of all those data

    # Let's create a candlestick chart

    # Give it title
    title = "ETH and BTC"
    Pl.candlestickPlot(ohlcv, title)


def binancePlots():

    # Let's make some basic plots now with our binance plotter
    # As before we get our ohlcv
    ohlcv = Ex.getBinanceOhlcv(symbol='BTC/USDT', limit=100, timeframe='15m')

    # Now we are going to extract from ohlcv every subarray (component)
    timestamp = Up.getTimestamp(ohlcv)
    openPrice = Up.getOpen(ohlcv)
    high = Up.getHigh(ohlcv)
    low = Up.getLow(ohlcv)
    close = Up.getClose(ohlcv)
    volume = Up.getVolume(ohlcv)

    # We are now plotting each different subbaray based on time
    Pl.timeDataPlot(timestamp, openPrice)
    Pl.timeDataPlot(timestamp, high)
    Pl.timeDataPlot(timestamp, low)
    Pl.timeDataPlot(timestamp, close)
    Pl.timeDataPlot(timestamp, volume)

