class Instructor: #class
    def __init__(self, instructor_name, address):
        self.name = instructor_name # attribute
        self.address = address # attribute
        self.followers = 0 # default attribute

instructor_1 = Instructor("John","London") # defining object
# instructor_1.name = "John"
# instructor_1.address = "London"

print(instructor_1.name)
print(instructor_1.followers)

instructor_2 = Instructor("Payal","Mumbai")
# instructor_2.name = "Payal"
# instructor_2.address = "Mumbai"
print(instructor_2.name)

instructor_3 = Instructor("Stefany","Bangkok")
print(instructor_3.name)
print(instructor_3.address)

instructor_4 = Instructor("Sohail","Kolkata")
print(instructor_4.name)
print(instructor_4.address)