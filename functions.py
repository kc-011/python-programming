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
   
