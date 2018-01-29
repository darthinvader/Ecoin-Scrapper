from datetime import datetime
import matplotlib.dates as mdates
import time

# timestamp2UnixEpoch
# arguments a timestamp array
# returns the timestamp array from binance timestamp to unix epoch


def timestamp2UnixEpoch(timestamp):
    timestamp = [int(str(x)[:-3]) for x in timestamp]
    return timestamp

# timestamp2num
# Takes the timestamps and converts it to num and then returns it


def timestamp2Num(timestamp):
    timestamp = timestamp2UnixEpoch(timestamp)
    timestamp = mdates.epoch2num(timestamp)
    return timestamp

# timestamp2Date
# Arguments:
# ohlcv:containing the arrays of screenshots of data
# return the timestamps in the format of Year-Month-Day Hour-Minute-Seconds


def timestamp2Date(timestamp):
    timestamp = timestamp2UnixEpoch(timestamp)
    dates = [datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in timestamp]
    return dates

# num2epoch
# takes a num date and returns Unix epoch


def num2Epoch(num):
    timestamp = mdates.num2epoch(num)
    return timestamp

# date2Epoch
# takes the date and transforms it into Unix Epoch


def date2Epoch(date):
    timestamp = [(time.mktime(datetime.strptime(x, '%Y-%m-%d %H:%M:%S').timetuple())) for x in date]
    return timestamp


# date2Timestamp
# Arguments:
#  return the timestamps in the format of Year-Month-Day Hour-Minute-Seconds


def date2Timestamp(date):
    timestamp = [(time.mktime(datetime.strptime(x, '%Y-%m-%d %H:%M:%S').timetuple()))*1000 for x in date]
    return timestamp


# unixEpoch2Date
# takes a unixEpoch and returns it into string dates


def unixEpoch2Date(timestamp):
    dates = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return dates


# unixEpoch2Dates
# takes a unixEpoch and returns it into string dates


def unixEpoch2Dates(timestamp):
    dates = [datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in timestamp]
    return dates
