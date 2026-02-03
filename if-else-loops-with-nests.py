#Going to come up with my own code and calculate the result

#If-Else statements
x = int(input("What's your age: "))
if x < 40:
    if x < 35:
        print("Lower than middle")
    else:
        print("Middle aged I guess")
else:
    print("Oldie")


if x >= 30:
    print("A")
if x >= 40:
    print("B") # these are 2 separate conditional statements - they are only attached by 
else:          # indentation or MAINLY by an 'elif' statement
    print("C")


if x < 30:
    print("You have time")
elif x == 30:
    print("You're almost halfway")
else:
    print("Count your days...")

#Let's take a math one - print number X(based on your input) with these
#Conditions: 1) if x is divisible by 3, print "Fizz"
#2) If x is divisible by 5, print "Buzz"
#3) if x is divisble by 3 and 5, print "FizzBuzz"
#4) if none of the above, print the number

if x % 3 == 0:
    if x % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(f"Your age is {x}")

#If we use logical operators, the most important conidition (#3) is put first

if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)

#lets come up with random stuff

if x in range(41):
    print("it's actually chill")
elif 50 > x >= 41: #comparison chaining
    print("nah you dying")
else:
    print("byebye")

#what will this print 
""" 
if "hello":
    print("yes")
else:
    print("bye")
"""

#you can use not/! also
"""
if x % 2 != 0 
or 
if not x % 2 == 0
"""

#if with falsy values is super imp
#falsy values: False, 0, 0.0, None, "", [], etc. (empty data structures)

# == compares value (are they the same value of the same type)
# is compares identity (same object)

#what will this print?
if x is not None:
    print("Some value")
if x:
    print("Really some value")

#Out of all the falsy values, only 0 == False is True because booleans
# are a subset of int, anything else will be false

#No falsy values are of the same object as the others so all are False
# unless specified (if x = None, then X is None = True)

#'is' is usually used with None only, since there is only one
# object of None 
