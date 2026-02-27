class Instructor:
    followers = 0 # Class Object Variable - applies to every object
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.followers = 0
    
    def display(self, subject_name): #function becomes method when it is attached to an object
         print(f"Hi, I am {self.name} and I teach {subject_name}")

    def update_followers(self, follower_name):
        self.followers += 1

instructor_1 = Instructor("John", "London")
print(instructor_1.name)
instructor_1.display("Football")
instructor_1.update_followers("Payal")
print(instructor_1.followers)

instructor_2 = Instructor("Payal","Mumbai")
instructor_2.display("Dance")
print(instructor_2.followers)
instructor_2.update_followers("Jenny")
print(instructor_2.followers)

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        self.area = self.pi * (radius**2)
    
    #def area(self):
        #return round(self.pi * (self.radius **2),2)
    #def circumference(self):
        #return round(2*self.pi*self.radius,2)
    
Circle_1 = Circle(4)
print(Circle_1.area)
#print(Circle_1.area())
#print(Circle_1.circumference())

class A:
    x = 5

a = A()
A.x = 20

print(a.x)

class Demo:
    def show(self):
        print("Hello")

d = Demo()
Demo.show(d)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount < 1:
            print("Please input an amount greater than 0")
            return
        
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return
        if amount <= 0:
            print("Please input an amount greater than 0")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
    
    def display(self):
        print("Owner:" , self.owner)
        print("Balance:" , self.balance)
    
    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return
        if amount <= 0:
            print("Please input an amount greater than 0")
            return
        self.balance -= amount
        other_account.balance += amount
        self.transactions.append(f"Transferred {amount} to {other_account.owner}")

    def history(self):
        for i in self.transactions:
            print(i)
acc1 = BankAccount("Karan", 2000)
acc2 = BankAccount("Rahul", 1000)

acc1.deposit(500)
acc1.display()

acc1.withdraw(400)
acc1.display()

acc1.transfer(acc2, 500)
acc1.display()
acc2.display()

acc1.history()