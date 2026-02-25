class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_nose = 1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")

male_1 = Male("Karan")
male_1.eat()
male_1.work()
print(male_1.num_eyes)
