import random
import yfinance as yf
from termcolor import colored
import time
import keyboard

idk = yf.download(tickers="AAPL", interval="5m", start="2026-03-31", end="2026-04-01")
aapl_values = []
for i in idk.iloc[:, 0:1]:
    for j in idk[i]:
        aapl_values.append(j)

min_val = min(aapl_values)
max_val = max(aapl_values)

scaled_aapl = []
for i in aapl_values:
    scale = i - min_val
    range_ = max_val - min_val
    pos_ = scale/range_
    map_ = pos_ * 19
    new_y = round(19 - map_)
    scaled_aapl.append(new_y)

width = len(scaled_aapl) #columns
height = 20 #rows

green_count = 0
red_count = 0
list2 = [[" " for i in range(width)] for i in range(height)]

y = scaled_aapl[0]
for x in range(width):
    if keyboard.is_pressed('space'):
        break
    prev_y = y
    y = scaled_aapl[x]
  
    y = max(0, min(height - 1, y))
    if y < prev_y:
            for i in range(prev_y-1, y-1, -1):
                list2[i][x] = colored("|", "green")
                green_count += 1

    if prev_y < y:
            for i in range(prev_y,y):
                list2[i][x] = colored("|", "red")
                red_count +=1
    
    if prev_y == y:
         list2[y][x] = colored("‾", "blue")

    print("\033[1;1H", end="")
    for row in list2:
        print("".join(row))
        time.sleep(0.01)
    print("Press the Spacebar to stop")
    print("\033[K""Green Candles:" , green_count) #added ANSI code to clear line because both digits 
    # were not getting cleared from previous run
    print("\033[K""Red Candles:" , red_count)

if green_count > red_count: #for profit
    multiplier = green_count - red_count #for loss
elif red_count > green_count:
    multiplier = red_count - green_count
else:
    multiplier = 0