class Account:
    #prices of stock - name them according to the popular ones
    stock_1 = 100
    stock_2 = 400
    stock_3 = 1200
    def __init__(self, username, shares):
        self.username = username
        self.balance = 10000
        self.shares = shares
    def buy_stock(self, stock, num):
        if stock*num < self.balance:
            return "Insufficient funds. Try buying a lower number of shares"

        self.balance -= (stock * num)
        self.shares += num
    def sell_stock(self, stock, num):
        self.balance += (stock*num)
        self.shares -= num

#while True:
print("----------------------\nStock Market Simulator\n----------------------\n")
