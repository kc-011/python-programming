#instead of writing the same code again and again, we can use function calling

#instead of print("Welcome to IDS Infotech") again & again
def welcome():
    return "Welcome to IDS Infotech"

print(welcome())

#OR 

def welcome():
    print("Welcome to IDS Infotech")

welcome()

#inside the () defined in the function, we can define parameters (defined variables)

def evenOrOdd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

print(evenOrOdd(5)) 
print(evenOrOdd(14)) #5 and 14 are arguments (actual values passed to the function) 

#we can have fixed arguments too
#Default Arguments:
def addTwo (x, y=2):
    return x + y

print(addTwo(4))
print(addTwo(7,4)) #we can overwrite the fixed argument

#Keyword Arguments:
def name(fname, lname):
    print(fname, lname)

#values are passed by specifying the parameter names, so the order doesn’t matter
name(fname="Karan", lname="Chawla")
name(lname="Chawla", fname="Karan")

#if we dont specify the parameter, the function will assign it in order
#This is called Positional Arguments:
name("Chawla", "Karan")

#if we dont know how many arguments will be passed, we use *args and *kwargs

#*args (Non-keyword arguments, aka positional arguments):
def sum(*args): #can replace args with any variable name
    total = 0
    for i in args: #all arguments are passed into a tuple, which is why we need to iterate
        total += i
    
    print(f"The numbers passed are {args}") 
    print(f"The sum of the numbers is {total}")

sum(2,4,67,3,9)
sum(1,4,3)

#**kwargs (Keyword arguments)
def clientInfo (**kwargs):
    print(kwargs) #is stored as a dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")

clientInfo(name="KC", age="22", school = "SFHS")

#Missing required arguments → TypeError

#order of paramters defined also matter:
# def func(a, b=10, *args, **kwargs):
    # a        -> required
    # b=10     -> default
    # *args    -> extra positional (tuple)
    # **kwargs -> keyword args (dict)


#DECORATORS
#used to wrap a function inside a function 
#for example, we have multiple processes running and need to show that it has started 
# and ended

def run(func):
    def wrapper(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Ending")
        return result
    return wrapper

@run
def add(a,b):
    return a+b

print(add(2,3))

#unclear^ come back later


#SCOPES
x = 10

def func():
    if False:
        x = 20
    print(x)
#this will not work because the local variable found at compile time is missing at runtime and
# global variable is ignored due to LEGB
#UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

#solution:
x = 10

def func():
    global x #this line
    if False:
        x = 20
    print(x)

func()

#same goes for enclosing functions
def outer():
    x = 10

    def inner():
        x = x + 1
        print(x)

    inner()

#same error above too for the same reason
#solution:
def outer():
    x = 10

    def inner():
        nonlocal x #this statement !!
        x = x + 1
        print(x)

    inner()

outer()

#In the code below, LEGB doesn't really play a role but the fact that the variable is trying
# to be printed before it was assigned is the problem 

def func():
    print(x)
    x = 10 #Unbound Local Error

x = 10
def fun():
    global x
    x = 15
fun()
print(x) #Here, even though our print statement is outside, once the function is called,
# the value of the variable is changed (due to 'global x')

#LAMBDA Functions
#they are used for much smaller functions or for functions within a function
#can have only one expression

x = lambda a : a + 10
print(x(7))
y = lambda a, b : a+b
print(y(1,1))

#let's say i want to make a multiplier, but i don't know which mulitplier (2x,3x,etc) or 
# number i will multiply. we will make a function that takes a lambda function 

def multi(n):
    return lambda a : a*n

doubleMulti = multi(2)
print(doubleMulti(7))

tripleMulti = multi(3)
print(tripleMulti(9))

#LAMBDA functions are widely used with map(), filter() and sorted() funcs
#map() is a lazy way to avoid for loops or any kind of external iteration
#it iterates over the given data with a function
#example:

number = [1,2,3,4,5,6]

sq_number = list(map(lambda x : x**2, number))
print(sq_number)

#filter() returns the data which stands 'True' for the function

odd_num = list(filter(lambda x: x%2!=0, number))
print(odd_num)

#sorted() used for custom sorting 
fruit = ['apple', 'banana', 'lime', 'dragonfruit']
new_fruit = sorted(fruit, key = lambda x : len(x))
print(new_fruit)
