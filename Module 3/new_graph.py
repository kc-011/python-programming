import yfinance as yf
from termcolor import colored
import time
import keyboard


def stock_graph(stock, start, end, interval):
    stock_data = yf.download(tickers=stock, interval=interval, start=start, end=end)
    closing_values = []
    for i in stock_data.iloc[:, 0:1]:
        for j in stock_data[i]:
            closing_values.append(j)

    if closing_values == []:
         print("No data found")
         return None, None

    min_val = min(closing_values)
    max_val = max(closing_values)

    scaled_values = []
    for i in closing_values:
        scale = i - min_val
        range_ = max_val - min_val
        pos_ = scale/range_
        map_ = pos_ * 19
        new_y = round(19 - map_)
        scaled_values.append(new_y)

    width = len(scaled_values) #columns
    height = 20 #rows
    step = (max_val - min_val) / 19
    #green_count = 0
    #red_count = 0
    list2 = [[" " for i in range(width)] for i in range(height)]

    y = scaled_values[0]
    print("\033[2J\033[H", end="")
    for x in range(width):
        #if keyboard.is_pressed('space'):
            #break - dropped this idea
        prev_y = y
        y = scaled_values[x]
    
        #y = max(0, min(height - 1, y))
        if y < prev_y:
                for i in range(prev_y-1, y-1, -1):
                    list2[i][x] = colored("▐", "green")
                    #green_count += 1

        elif prev_y < y:
                for i in range(prev_y,y):
                    list2[i][x] = colored("▐", "red")
                    #red_count +=1
        
        else:
            list2[y][x] = colored("‾", "blue", attrs=["bold"])

        print("\033[1;1H", end="")
        for row_index, row in enumerate(list2):
            price = max_val - (row_index*step)
            price_label = f"{price:7.2f}"
            print(price_label + " | " + "".join(row))
            time.sleep(0.05)
        
        print(f"                                   Current price: {closing_values[x]}")
        #print("\nPress the Spacebar to stop")
        print("\nPress B to Buy | Press S to Sell")
        #print("\033[K""Green Candles:" , green_count) #added ANSI code to clear line because both digits 
        # were not getting cleared from previous run
        #print("\033[K""Red Candles:" , red_count)
        if keyboard.is_pressed('b'):
             print(f"Bought at {closing_values[x]}")
             return "buy", closing_values[x], stock_data
        if keyboard.is_pressed('s'):
             print(f"Sold at {closing_values[x]}")
             return "sell", closing_values[x], stock_data
    return None, closing_values[-1], stock_data
    '''
    # no point of this if we're using real values
    if green_count > red_count: #for profit
        multiplier = green_count - red_count #for loss
    elif red_count > green_count:
        multiplier = red_count - green_count
    else:
        multiplier = 0
    '''