
def calculateSMA(value, history):
    sma_array = []
    for i in range(len(history)):  # iterates currencies
        for x in range(len(history[i])-value):  # iterates minutes
            sum = 0
            for y in range(value):  # iterates from -value to 0 position in array for SMA calculation
                sum += history[i][(x+value-y)][0]
            history[i][x+value].append(sum/value)
    return history


