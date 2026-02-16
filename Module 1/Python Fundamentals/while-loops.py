"""n = int(input("Enter a number: "))

#Sum of First N Natural Numbers
sum = 1
count = 1
x = 1
while count < n:
    x += 1 
    sum += x #x is not needed, can sum 'count' to 'sum'
    count += 1
print(f"Sum of first {n} natural numbers is {sum}")"""

#Prime Number Checker
x = int(input("Enter a number: ")) 
divisor = 1
count = 0
while divisor <= x: 
    if x % divisor == 0:
        count +=1 
        divisor+=1 
        if count > 2:
            print(f"{x} is not a prime number")
            break
        elif count <= 2:
            if divisor > x:
                print(f"{x} is a prime number")
                break
        else:
            continue
    else:
        divisor+=1
 
 
#Print a message 3 times
"""message = input("Enter a message: ")
i = 0
while i < 3:
    print(message)
    i+=1"""

#Multiplication Table of a Number
"""n = int(input("Enter a number: "))
x = int(input(f"How many multiples do you want of {n}: "))
i = 0
j = 0
while i < x:
    j+=n
    i+=1
    print(f"{n} x {i} = {j}")"""

#Reverse a number
"""
n = int(input("Enter a number: "))
reverse = 0
x = 0
while n>0:
    x = n%10
    n = n // 10
    #y = y + str(x) #this is cheating a little bit
    reverse = (reverse*10) + x
print(reverse)
"""
#problems from 
# https://www.thevistaacademy.com/some-important-questions-about-the-while-loop-in-python-to-practice/?srsltid=AfmBOooQzYlikiy-YSFyhSzKRWJ0bLiRMdyluM0c26fAakNbhA_aM1qw