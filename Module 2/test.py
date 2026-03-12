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
        input1 = int(input("1. Show \n2. Delete \n3. Search \n4. Update \n5. Exit: "))
        if not 1<=input1<=5:
            print("Please input one of the following numbers only")
        #else:
            #break   
    except ValueError:
        print("Please enter a number")
    if input1 == 5:
        break
    if input1 == 1:
        StudentManagement.__repr__(self=student_list)
    if input1 == 2:
        del_input = int(input("Enter the ID of the student you want to delete: "))
        for i in student_list:
            if i.id == del_input:
                student_list.remove(i)
                print("Successfully Deleted")
        
            
            
