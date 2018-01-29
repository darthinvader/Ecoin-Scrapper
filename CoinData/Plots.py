import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc
from CoinData import TimeConvert as Tc
from CoinData import Unpack as Up
# ScatterPlot
# Arguments:
# close1: the array of closing prices for the first coin
# close2: the array of closing price for the second coin
# xlabel: the label used in the x axis for the plot
# ylabel: the label used in the y axis for the plot
# title: the title of the plot
# color: the color of the dots on the plot
# marker:the marker used for the dots on the plot (e.g 'o' is for circle) same as matplotlib
# size: the size of the marker
# The function shows a scatter plot of the data given


def scatterPlot(close1, close2, xlabel="", ylabel="", title="Correlation Plot", color='k', marker='o', size=40):
    plt.scatter(close1, close2, label="CorrPlot", color=color, marker=marker, s=size)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# formatMake is a function used for Plots
# not to be used from outside
# it takes the timestamp and returns the format in which the date is shown


def formatMake(ohlcv):
    timeframes = len(ohlcv)
    timedif = ohlcv[0][0] - ohlcv[1][0]
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
# Note candlestickPlot takes ages to run

def candlestickPlot(ohlcv, title="stock"):
    dateFormat = formatMake(ohlcv)

    title += " begins: " + Tc.unixEpoch2Date(ohlcv[0][0])
    widthMul = (ohlcv[0][0] - ohlcv[1][0]) / 60
    width = (widthMul * 0.005) / (len(ohlcv) + 5)

    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ohlcv = ohclvForPlots(ohlcv)
    candlestick_ohlc(ax1, ohlcv, width=width, colorup='#00FF00', colordown='#FF0000')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter(dateFormat))
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(title)
    plt.show()

# timeDataPlot
# Arguments:
# ohlcv:containing the arrays of screenshots of data
# The function shows a normal plot of the data relative to time


def timeDataPlot(timestamp, data):
    dateFormat = formatMake(timestamp)
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    timestamp = Tc.timestamp2Num(timestamp)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter(dateFormat))
    ax1.plot(timestamp, data)
    plt.show()

# ohlcvForPlots
# Takes a ohclv and converts its timestamp to num timestamp


def ohclvForPlots(ohlcv):
    timestamp = Up.getTimestamp(ohlcv)
    timestamp = mdates.epoch2num(timestamp)
    size = len(ohlcv)
    for i in range(0, size):
        ohlcv[i][0] = timestamp[i]
    return ohlcv
