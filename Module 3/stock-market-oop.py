class Account:
    #prices of stock - name them according to the popular ones
    stock_1 = 100
    stock_2 = 400
    stock_3 = 1200
    def __init__(self, username, password, message):
        self.username = username
        self.password = password
        self.message = message #to debug/check object
        self.balance = 10000
        self.shares = 0
        self.transactions = []
        users.append(self)

    def show_balance(self):
        print(f"Current balance: {self.balance}. I am {self.message}")
        return
    
    def history(self):
        if self.transactions == []:
            print("Nothing to show here!")
        else:
            for i in self.transactions:
                print(i)

#what am i even doing in these two methods below ??

    def buy_stock(self, stock, num):
        if stock*num > self.balance:
            return "Insufficient funds. Try buying a lower number of shares"

        self.balance -= (stock * num)
        self.shares += num
        self.transactions.append(f"Bought {num} number of shares")
    
    def sell_stock(self, stock, num):
        self.balance += (stock*num)
        self.shares -= num
        self.transactions.append(f"Sold {num} number of shares")

users = []
demo_account = Account("IDS-Trainee", "Login@#123", "demo")
private_account = Account("kc11", "chawla05", "private")
#while True:
print("----------------------------\n📈 Stock Market Simulator 📉\n----------------------------")
print("Hi, please choose the account you would like to use\n1. IDS-Trainee\n2. kc11")

while True:
    try:
        user_name = int(input("---> "))
    except ValueError:
        print("Please enter a number")
    else:
        if user_name == 1:
            current_account = demo_account
            break
        elif user_name == 2:
            current_account = private_account
            break
        else:
            print("Please input a valid option")

current_account.buy_stock(1200,5)

print()
while True:
    print()
    print("What would you like to do today?\n\n1. Check Balance\n2. Check Transactions\n3. Sell your share\n4. Buy a share\n5. Switch Accounts\n")
    try:
        userinput = int(input("---> "))
    except ValueError:
        print("Please enter a number")
    else:
        if userinput < 1 or userinput > 5:
            print("Please enter one of the above options only")
        elif userinput == 1:
            current_account.show_balance()
        elif userinput == 2:
            current_account.history()
        elif userinput == 5:
            if user_name == 1:
                current_account = private_account
                print("Account switched to kc11")
            else:
                current_account = demo_account
                print("Account switched to IDS-Trainee")
        else:
            break

#I want to implement login system where the user can choose from either of the 2 accounts and then can 
# do anything. maybe also the option to switch accounts somehow. Hurry up!! deadline - 2nd April