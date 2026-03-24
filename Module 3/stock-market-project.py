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

'''import random
import time

pos = 10  # starting position (middle-ish)
width = 20  # limits

for _ in range(50):  # number of steps
    move = random.choice(["/", "\\"])
    
    if move == "/":
        pos -= 1
    else:
        pos += 1

    # keep it within bounds
    if pos < 0:
        pos = 0
    if pos > width:
        pos = width

    print(" " * pos + move)
    time.sleep(0.1)'''

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
width = 10 #columns
height = 10 #rows
#with list comprehension
list2 = [[" " for i in range(height)] for i in range(width)]
#print(list2)

#list2[2][5] = "X"

y = height // 2
for x in range(width):
    move = random.choice([-1,1]) #-1 UP, 1 DOWN
    y += move
    y = max(0, min(height - 1, y))
    if move == -1:
        list2[y][x] = "/"
    else:
        list2[y][x] = "\\"

for i in list2:
    print("".join(i))
