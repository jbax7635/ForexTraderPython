def readData():
    with open("C:\Users\John\Desktop\Programming\fromEA") as f:
        line = f.readlines()
        newlist = [lines.split(',')[-2:-1] for lines in line]  # list of minute data list
    print(newlist)