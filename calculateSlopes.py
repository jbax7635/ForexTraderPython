def getSlopes(SMAlist, slopeInterval, SMA):
    for x in range(len(SMAlist)):  # iterates through each currency
        # iterates through each minute in each currency
        length = int(slopeInterval[len(slopeInterval)-1])
        if length < 0:
            length = length * -1
        length += SMA
        for i in range(length, len(SMAlist[x])-length):
            for y in range(len(slopeInterval)):  # iterates the slope interval list
                #  calculates and inserts slope values at given interval
                slope = (SMAlist[x][i][1]-SMAlist[x][i-slopeInterval[y]][1])/slopeInterval[y]
                SMAlist[x][i].append(slope)
    return SMAlist


def square_off_array(SMAlist):
    returnable_array = []
    for i in range(len(SMAlist)):
        size = 0
        array = []
        for x in range(len(SMAlist[i])):
            if len(SMAlist[i][x]) > size:
                size = len(SMAlist[i][x])
        for y in range(len(SMAlist[i])):
            if len(SMAlist[i][y]) == size:
                array.append(SMAlist[i][y])
        returnable_array.append(array)
    return returnable_array

