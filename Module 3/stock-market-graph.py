'''import random

def random_str(length, chars):
    random_string = ""
    for i in range(length):
        random_string += random.choice(chars)
    return random_string

test1 = random_str(8, "/\\")
print(test1)'''

'''import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)'''

'''
[][][][][][][]
[][][][][][][]  need to create this
[][][][][][][]
[][][][][][][]
'''

'''list1 = []
list3 = []
for x in range(5):
    for i in range(11):
        list1 += [" "]
    list3 += list1
print(list3)'''

import random
# from rich.console import Console
# console = Console()
from termcolor import colored
import time
import keyboard

width = 50 #columns
height = 20 #rows
#with list comprehension
#list2 = [[" " for i in range(width)] for i in range(height)]
#print(list2)

#list2[2][5] = "X"
green_count = 0
red_count = 0
list2 = [[" " for i in range(width)] for i in range(height)]
y = height // 2
for x in range(width):
    if keyboard.is_pressed('space'):
        break
    if y == 0:
        move = 1
    elif y == height-1:
        move = -1
    else:
        move = random.choice([-1,1]) #-1 UP, 1 DOWN
    prev_y = y
    y += move
    y = max(0, min(height - 1, y))
    if y < prev_y:
        if move == -1:
            list2[y][x] = colored("/", "green")
            green_count += 1
        else:
            list2[y][x-1] = colored("\\", "red")
            red_count += 1
    if prev_y < y:
        if move == -1:
            list2[y][x] = colored("/", "green")
            green_count +=1
        else:
            list2[y-1][x] = colored("\\", "red")
            red_count +=1
    print("\033[1;1H", end="")
    for row in list2:
        print("".join(row))
        time.sleep(0.01)
    print("Press the Spacebar to stop")
    print("\033[K""Green Candles:" , green_count) #added ANSI code to clear line because both digits 
    # were not getting cleared from previous run
    print("\033[K""Red Candles:" , red_count)


# If you want to see graph printing in the same place, stretch the terminal to the top or atleast
# the same length as the grid