class Account:
    #prices of stock - name them according to the popular ones
    stock_1 = 100
    stock_2 = 400
    stock_3 = 1200
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 10000
        self.shares = 0
        self.transactions = []
        users.append(self)

    def show_balance(self):
        print(f"Current balance: {self.balance}")
        return
    
    def history(self):
        for i in self.transactions:
            print(i)

#what am i even doing in these two methods below ??

    def buy_stock(self, stock, num):
        if stock*num < self.balance:
            return "Insufficient funds. Try buying a lower number of shares"

        self.balance -= (stock * num)
        self.shares += num
        self.transactions.append(f"Bought {num} number of shares of (this company)")
    
    def sell_stock(self, stock, num):
        self.balance += (stock*num)
        self.shares -= num
        self.transactions.append(f"Sold {num} number of shares of (this company)")

users = []
#while True:
print("----------------------------\n📈 Stock Market Simulator 📉\n----------------------------")
#print("Hi, please enter your username")
#user_name = input("---> ")
demo_account = Account("IDS-Trainee", "Login@#123")
private_account = Account("kc11", "chawla05")
#print(users)


print()
print("What would you like to do today?\n\n1. Check Balance\n2. Check Transactions\n3. Sell your share\n4. Buy a share\n")
try:
    userinput = int(input("---> "))
except ValueError:
    print("Please enter a number")
else:
    if userinput < 1 or userinput > 4:
        print("Please enter one of the above options only")
if userinput == 1:
    #then show balance of logged in account
    pass
if userinput == 2:
    #then show transaction history of logged in account
    pass

#I want to implement login system where the user can choose from either of the 2 accounts and then can 
# do anything. maybe also the option to switch accounts somehow. Hurry up!! deadline - 2nd April