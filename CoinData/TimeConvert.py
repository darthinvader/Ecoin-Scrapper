from datetime import datetime
import matplotlib.dates as mdates
import time


# timestamp2Date
# Arguments:
# ohlcv:containing the arrays of screenshots of data
# return the timestamps in the format of Year-Month-Day Hour-Minute-Seconds

def timestamp2Date(timestamp):
    dates = [datetime.fromtimestamp(int(str(x)[:-3])).strftime('%Y-%m-%d %H:%M:%S') for x in timestamp]
    return dates


# date2Timestamp
# Arguments:
# date containing a single datetime
# return the timestamps in the format of Year-Month-Day Hour-Minute-Seconds


def date2Timestamp(date):
    timestamp = time.mktime(datetime.strptime(date, '%Y-%m-%d %H:%M:%S').timetuple())
    timestamp = int(timestamp * 1000)
    return timestamp


# timestamp2UnixEpoch
# arguments a timestamp array
# returns the timestamp array from binance timestamp to unix epoch

def timestamp2UnixEpoch(timestamp):
    timestamp = [int(str(x)[:-3]) for x in timestamp]
    return timestamp


# timestamp2num
# Takes the timestamps and converts it to num and then returns it

def timestamp2num(timestamp):
    timestamp = timestamp2UnixEpoch(timestamp)
    timestamp = mdates.epoch2num(timestamp)
    return timestamp


def unixEpoch2Date(timestamp):
    dates = [datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in timestamp]
    return dates
