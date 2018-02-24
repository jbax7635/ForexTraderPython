def find_optimal_trade(array):
    for i in range(len(array)):
        for x in range(len(array[i])):
            min_price = array[i][x][0]*.999  # adds small buffer for low point to be calculated from
            max_price = array[i][x][0]*1.001  # adds small buffer for low point to be calculated from
            low_reached = False
            high_reached = False
            print(x)
            print(array[i][x])
            for y in range(len(array[i][x]), len(array[i])):
                #  set new max if max reached and turn on high_reached
                if array[i][y][0] > max_price:
                    max_price = array[i][y][0]
                    high_reached = True
                #  set new min if min reached and turn on low_reached
                if array[i][y][0] < min_price:
                    min_price = array[i][y][0]
                    low_reached = True
                # expressions for breaking loop if both high and low have been set and price crossing starting point
                if array[i][y-1][0] > array[i][x][0] and array[i][y][0] < array[i][x][0] \
                        and high_reached is True and low_reached is True:
                    break
                if array[i][y-1][0] < array[i][x][0] and array[i][y][0] > array[i][x][0] \
                        and high_reached is True and low_reached is True:
                    break
            #  gets pip movement
            max_price -= array[i][x][0]
            min_price -= array[i][x][0]
            #  adjusts pip movement to max 500 pips
            if max_price > .05:
                max_price = .05
            if min_price < -.05:
                min_price = -.05
            array[i][x].append(max_price)
            array[i][x].append(min_price)
            print(array[i][x])
    print(array[0][2000])
    return array



