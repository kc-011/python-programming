class Student:
    def __init__(self, id, fname, lname, age, standard, marks):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.standard = standard
        self.__marks = marks
        student_list.append(self)

class StudentManagement(Student):
    def updatefname(self,fname):
        self.fname = fname
    
    def updatelname(self, lname):
        self.lname = lname

    def updateage(self, age):
        self.age = age
    
    def updatestandard(self, standard):
        self.standard = standard

    def __str__(self):
        print(f"ID: {self.id}, Full Name: {self.fname} {self.lname}, Age: {self.age}, Class: {self.standard}")
        #return super().__str__()
    
    def __repr__(self):
        for i in student_list:
            print(f"({i.id}, {i.fname} {i.lname})")
        #return super().__repr__()

student_list = []
student1 = StudentManagement(1, "Kartik", "Ahuja", 15, "7C", "82%")
student2 = StudentManagement(2, "Rohan", "Sharma", 17, "9B", "94%")
#print(student_list)
#student_list.append(student1)

'''
print(student1.fname)
print(student1.lname)

student1.updatefname("Karan")
student1.updatelname("Chawla")

print(student1.fname)
print(student1.lname)
'''
for i in student_list:
    if i.id == 1:
        print(i.age)

while True:
    try:
        input1 = int(input("1. Show \n2. Delete \n3. Search \n4. Update \n5. Exit:\n--> "))
        if not 1<=input1<=5:
            print("Please input one of the following numbers only")   
    except ValueError:
        print("Please enter a number")
    
    if_found = False
    if input1 == 5:
        break

    if input1 == 1:
        StudentManagement.__repr__(self=student_list)
    
    if input1 == 2:
        del_input = int(input("Enter the ID of the student you want to delete: "))
        for i in student_list:
            if i.id == del_input:
                student_list.remove(i)
                if_found = True
        if if_found:
            print("Successfully removed")
        else:
            print("Not found")

    if input1 == 3:
        search_input = int(input("Enter the ID of the student you want to search: "))
        for obj in student_list:
            if obj.id == search_input:
                StudentManagement.__str__(obj)

    if input1 == 4:
        update_input1 = int(input("Enter the ID of the student you want to update: "))
        for obj in student_list:
            if obj.id == update_input1:
                update_input2 = int(input("Which field would you like to update:\n1. First name\n2. Last name\n3. Age\n4. Standard\n--> ")) 
                if update_input2 == 1:
                    fname_input = input("Enter first name: ")
                    obj.updatefname(fname_input)
                if update_input2 == 2:
                    lname_input = input("Enter last name: ")
                    obj.updatelname(lname_input)
                if update_input2 == 3:
                    age_input = input("Enter Age: ")
                    obj.updateage(age_input)
                if update_input2 == 4:
                    standard_input = input("Enter Standard: ")
                    obj.updatestandard(standard_input)

'''
Some stuff I would like to add:
1. a 'Go back' option so that user can exit that function at any time 
2. Maybe a random ID generator for the students (I'll be able to see the ID using show() func) 
but it must be unique for all objects
3. If there's anything else I can do for add func and not make it complicated
4. Try except blocks for every user input (this will take years) - some simplified version maybe

TBC
'''