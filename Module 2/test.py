class Student:
    def __init__(self, id, fname, lname, age, standard, marks):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.standard = standard
        self.__marks = marks

class StudentManagement(Student):
    def updatefname(self,fname):
        self.fname = fname
    
    def updatelname(self, lname):
        self.lname = lname

    def updateage(self, age):
        self.age = age
    
    def updatestandard(self, standard):
        self.standard = standard
    
    def deleteObj(self):
        del self

student_objs = []
student1 = StudentManagement(1, "Karun", "C", 15, "8B", "82%")

student_objs.append(student1)


print(student1.fname)
print(student1.lname)

student1.updatefname("Karan")
student1.updatelname("Chawla")

print(student1.fname)
print(student1.lname)


