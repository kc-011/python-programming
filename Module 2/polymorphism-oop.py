class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

def make_sound(obj):
    obj.sound()

#polymorphism - same method, different objs/types (aka same interface, different behaviour)
make_sound(Dog())
make_sound(Cat())

#these are the standard ways to call it
dog1 = Dog()
dog1.sound()

make_sound(dog1)

#Abstraction - hides complexity of code (not making a file on it yet, only theory)