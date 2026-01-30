word = "hey" #string
time = 5 #int
true_time = 5.30 #float
is_it_time_to_sleep = False #boolean (0 is false)
is_it_time_to_work = True #boolean (1 is True)
complex_no = 4 + 3j #real number + (imaginary number)j

#OPERATIONS WITH ABOVE DATA TYPES

#with String
#Addition (+)
new_word = word + " whats up" #result: hey whats up
"""new_word_1 = word + time""" #error - can't cat string & int
"""name = input("What's your name?: ")""" #used for input
"""print(new_word , name)""" #don't use +, it will join the strings

#you can change the type of a variable then concatenate it
print(new_word + ". people usually leave by" , str(time)+":30")

#Multiplication (*)
print(word * 4)
many_words = word * 3 + "ho" * 3
print(many_words) #self-explained

#Multiplication with float is NOT allowed.

#what if we do 
word_into_0 = word * 0 #result?
print("word * 0 =", word_into_0)
#or word * -1 ? what is the result

#Subtraction(-) and Division(/) do not apply to strings

#Empty strings
#"" is false
#" " is true

#with Integers
#Addition, Subtraction and Multiplication - Straightforward

#Division
print(8/4) #division will always return a float
print(6//4) #FLOOR division where it gets rounded down (1.5 -> 1)
#but does not return a float, only int
print(7%2) #mod - remainder of 7/2
#sign of result is always same as the divisor
#-7%2=1
#7%-2=-1
print(2**3) #exponents 

"""
#Relational (Comparison) Operations
5 > 3     # True
5 < 3     # False
5 == 5    # True
5 != 3    # True
5 >= 5    # True
5 <= 4    # False

#Logical Operations
bool(0)    # False
bool(5)    # True
bool(-3)   # True

5 and 3    # 3
0 and 5    # 0
5 or 0     # 5
0 or 7     # 7
not 5      # False
not 0      # True

#Assignments Operations
x = 5
x += 2   # 7
x -= 1   # 6
x *= 2   # 12
x //= 2  # 6
x %= 4   # 2
x **= 2  # 4

#Order (high → low):

1. **
2. ~            ← bitwise NOT
3. *  /  //  %
4. +  -
5. <<  >>
6. &
7. ^
8. |
9. Comparisons (==, !=, <, >, <=, >=)
10. not
11. and
12. or
"""

#Bitwise and logical ops have different syntax
print(5 and 3) #logical
print(5 & 3) #bitwise
print(3<<2) #left shifting
print(4>>3) #right shifting
