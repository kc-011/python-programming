#Base/Parent/Super class --> Derived/Child/Sub class

class Human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name, num_heart):
        super().__init__(num_heart)
        self.name = name
    def jump(self):
        print("I can jump")
    def work(self):
        super().work()
        print("I can code")

male_1 = Male("Karan",1)
male_1.eat()
male_1.work()
print(male_1.num_heart)
