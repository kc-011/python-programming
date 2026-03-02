#Base/Parent/Super class --> Derived/Child/Sub class

#Single Inheritance
#Parent 1 --> Child 1

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
        super().work() #used so you can call parent & child method at the same time
        print("I can code")

male_1 = Male("Karan",1)
male_1.eat()
male_1.work()
print(male_1.num_heart)


#Multiple Inheritance
#Parent 1 and Parent 2 --> Child 1

class People:
    def run(self):
        print("I can run")
    def eat(self):
        print("I need to eat")

class Female:
    def work(self):
        print("I can work")
    def eat(self):
        print("I can eat")

class Girl(Female, People):
    def run(self):
        print("I can run faster")
    def drink(self):
        print("I can drink faster")

#Clearly, there are methods above being overridden
#The method is called based on the order of the parent class called in the child class

girl_1 = Girl()
girl_1.eat() #called from 'Female'
People.eat(girl_1) #manually called since 'Female' method overrides 'People' due to order
girl_1.run()
People.run(girl_1)

#MRO - Method Resolution Order
#How the interpreter searches for methods & in which order
#We can check by using the mro func

print(Girl.mro())

#First it searches for the method in 'Girl' then 'Female' then 'People'
#MRO will change if i change the class to Girl(People, Female)

#Mutlilevel Inheritance
# Parent --> Child 1 --> Child 2 --> ...

class A:
    def __init__(self,age):
        self.age = age
        self.number1 = 1
        self.number2 = 2
    def Intro(self):
        print("Hi, I am A")

class B(A):
    def __init__(self, height):
        self.height = height
        self.time = 4
    def Me(self):
        print("Hi, I am B")

class C(B):
    def __init__(self,name,age,height):
        #super().__init__() can be written as the line below too
        A.__init__(self,age)
        B.__init__(self,height)
        self.name = name
    def Myself(self):
        print("Hi, I am C")
    def display(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old")

c_1 = C("Caca",5,4.5)
c_1.Myself()
c_1.Me()
c_1.Intro()
print(c_1.number1)
c_1.display()
print(c_1.time)

#MRO in above example - C, B, A

#Hierarchical Inheritance 
#Parent 1 --> Child 1
#Parent 1 --> Child 2
#Parent 1 --> Child 3 ....
#Opposite of Multiple Inheritance

#Can be seen in the code I did below

#Question from Jenny OOPS lecture 93
#Ans:

class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name
    def ShowDetails(self):
        print(f"Hi, this is {self.uni_name}")
    
class Course(University):
    def __init__(self, uni_name, course):
        University.__init__(self, uni_name)
        self.course = course
    def ShowDetails(self):
        University.ShowDetails(self)
        print(f"We offer {self.course} at {self.uni_name}")

class Branch(University):
    def __init__(self, uni_name, branch):
        University.__init__(self, uni_name)
        self.branch = branch
    def ShowDetails(self):
        University.ShowDetails(self)
        print(f"This is the {self.branch} branch at {self.uni_name}")
    
class Student(Course, Branch):
    def __init__(self, uni_name, course, branch,name):
        Course.__init__(self, uni_name, course)
        Branch.__init__(self, uni_name, branch)
        self.name = name
    def ShowDetails(self):
        Course.ShowDetails(self)
        Branch.ShowDetails(self)
        print(f"I am {self.name} studying {self.course} in the {self.branch} branch")

class Faculty(Branch):
    def __init__(self, uni_name, branch, faculty):
        branch.__init__(uni_name, branch)
        self.faculty = faculty
    def ShowDetails(self):
        Branch.ShowDetails(self)
        print(f"The teacher is {self.faculty} from {self.branch} branch")

student_1 = Student("HWU", "Computer Science", "MACS", "Karan Chawla")
student_1.ShowDetails()