from new_graph import stock_graph

class Account:
    #prices of stock - name them according to the popular ones
    #stock_1 = 100
    #stock_2 = 400
    #stock_3 = 1200
    def __init__(self, username, password, message):
        self.username = username
        self.__password = password
        #self.message = message #to debug/check object
        self.balance = 10000
        self.portfolio = {}
        self.transactions = []
        users.append(self)

    def show_balance(self):
        print(f"Current balance: {self.balance:.2f}")
        return
    
    def show_portfolio(self):
        if self.portfolio == {}:
            print("No stocks owned")
            return
        
        print("Your Portfolio:\n")
        for stock, num in self.portfolio.items():
            print(f"{stock}: {num} shares")

    
    def history(self):
        if self.transactions == []:
            print("Nothing to show here!")
        else:
            for i in self.transactions:
                print(i)

#what am i even doing in these two methods below ?? ---> i fixed it now

    def buy_stock(self, stock, price, num):
        total = price * num
        if total > self.balance:
            print("Insufficient funds. Try buying a lower number of shares")
            return

        self.balance -= total
        self.portfolio[stock] = self.portfolio.get(stock, 0) + num
        self.transactions.append(f"Bought {num} shares of {stock} at price of {price:.2f}")

        print("Bought Successfully!")
    
    def sell_stock(self, stock,price, num):
        if stock not in self.portfolio:
            print("You don't have this stock")
            return
        if self.portfolio[stock] < num:
            print("Not enough shares")
            return 
        
        self.balance += price*num
        self.portfolio[stock] -= num
        if self.portfolio[stock] == 0:
            del self.portfolio[stock]
        self.transactions.append(f"Sold {num} shares of {stock} at {price:.2f}")

        print("Sold Successfully!")

def export_csv(stock_data, stock, start_input):
    filename = f"{stock}_{start_input}_data.csv"
    stock_data.to_csv(filename)
    print("CSV file created")

def export_txt(stock_data, stock, start_input):
    filename = f"{stock}_{start_input}_data.txt"
    with open(filename, "w") as f:
        f.write(stock_data.to_string())
    print("TXT file created")

def export_data(stock_data, stock, start_input):
    print("\n1. CSV")
    print("2. TXT")

    choice = input("---> ")

    if choice == "1":
        export_csv(stock_data, stock, start_input)
    elif choice == "2":
        export_txt(stock_data, stock, start_input)
    else:
        print("Invalid choice")
users = []
demo_account = Account("IDS-Trainee", "Login@#123", "demo")
private_account = Account("kc11", "chawla05", "private")
#while True:
print("\033[2J\033[H", end="")
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

#current_account.buy_stock(1200,5)


while True:
    print()
    print(f"What would you like to do today @{current_account.username} ?\n\n1. Check Balance\n2. Check Transactions\n3. Show Portfolio\n4. Trade\n5. Switch Account\n6. Exit")
    try:
        userinput = int(input("---> "))
    except ValueError:
        print("Please enter a number")
    else:
        if userinput < 1 or userinput > 6:
            print("Please enter one of the below options only")
        elif userinput == 1:
            current_account.show_balance()
        elif userinput == 2:
            current_account.history()
        elif userinput == 3:
            current_account.show_portfolio()
        elif userinput == 4:
            stock_input = input("Enter a stock (AAPL/MSFT/TSLA): ").upper()
            start_input = input("Enter Start date (YYYY-MM-DD): ")
            end_input = input("Enter End date (YYYY-MM-DD): ")
            interval_input = input("Enter Interval (15m/1h/1d): ")

            action, price, stock_data = stock_graph(stock_input, start_input, end_input, interval_input)
            if action is None:
                print("No action taken")
            else:
                try:
                    num = int(input("Enter quantity: "))
                except:
                    print("Invalid quantity")
                    continue

                if action == "buy":
                    current_account.buy_stock(stock_input, price, num)

                elif action == "sell":
                    current_account.sell_stock(stock_input, price, num)
            
            export = input("Export data? (y/n): ")

            if export.lower() == "y":
                export_data(stock_data, stock_input, start_input)
        
        elif userinput == 5:
            if user_name == 1:
                current_account = private_account
                print("Account switched to kc11")
                user_name = 2
            else:
                current_account = demo_account
                print("Account switched to IDS-Trainee")
                user_name = 1
        else:
            print("Thank you for using KC Stock Market Simulator 💫")
            break
#I want to implement login system where the user can choose from either of the 2 accounts and then can 
# do anything. maybe also the option to switch accounts somehow. Hurry up!! deadline - 2nd April