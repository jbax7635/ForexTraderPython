def gethistory(temp):
    returnable = []
    # loop which iterates each currency pair
    for i in range(len(temp)):
        # loop which reads forex history files in exact format and returns close prices and splits
        temp_returnable = []
        with open(temp[i]) as f:
            line = f.readlines()
            newlist = [lines.split(',')[-2:-1] for lines in line]  # list of minute data list
        for x in range(len(newlist)):
            temp_returnable.append([float(newlist[x][0])])
        returnable.append(temp_returnable)
        # print(len(returnable[0]))
        # exit()
    return returnable







