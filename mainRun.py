
import getHistory
import fillSimpleMovingAverage
import calculateSlopes
import optimal_trade_calc
import numpy
import scipy


# String list of file locations to upload
currencyPairs = ["C:\\Users\\John\\desktop\\Programming\\EURUSD.txt"]

# Strings to be passed to the text file for trading (mql4)
StringCurrencyPairs = ["EUR/USD"]

# Slope Sequence, the periods in time that the software looks at ie, look at the price 2 minutes ago and 5 minutes ago
# Future variables to play with and adjust
slopeSequence = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
negativeSlopeSequence = [i*-1 for i in slopeSequence]


# Simple Moving Average Value
SMA = 5

# upload all historical data from "currencyPair" files
# history[currency][minute][close, "value"sma]
raw_history = getHistory.gethistory(currencyPairs)



# calculate a 5 SMA moving average from close prices and return array
SMA_array = fillSimpleMovingAverage.calculateSMA(SMA, raw_history)


# calculate slopes for data and fill array
full_history = calculateSlopes.getSlopes(SMA_array, slopeSequence, SMA)

# calculate future slopes
history_with_trades = calculateSlopes.getSlopes(SMA_array, negativeSlopeSequence, SMA)

# square off array
#history = calculateSlopes.square_off_array(history_with_trades)
print(full_history[0][1])


# LOOP FROM HERE
# Read EA trade commands & clean file
# Classify history array relative to incoming price (group like prices and make new array)
# Calculate optimal Trade
# Write commands


