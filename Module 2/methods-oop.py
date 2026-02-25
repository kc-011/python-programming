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

