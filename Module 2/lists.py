#Create a list of numbers from 1 to 20
print([i for i in range(1,21)])

#Create a list of squares from 1 to 10.
print([i**2 for i in range(1,11)])

#Create a list of cubes of numbers from 1 to 10.
print([i**3 for i in range(1,11)])

#Create a list of even numbers from 1 to 50.
print([i for i in range(1,51) if i % 2 == 0])

#Create a list of numbers divisible by 3 from 1 to 50.
print([i for i in range(1,51) if i % 3 == 0])

#Create a list of squares of odd numbers from 1 to 20.
print([i**2 for i in range(1,21) if i % 2 != 0])

#From 1 to 10:
#If number is even → keep it
#If number is odd → replace with 0
print([i if i % 2 == 0 else 0 for i in range(1,11) ])

#From 1 to 15:
#If divisible by 3 → write "Fizz"
#Otherwise → keep number
print(["Fizz" if i % 3 == 0 else i for i in range(1,16)])

words = ["apple", "banana", "cat", "dog", "elephant"]
print([len(i) for i in words])
print([i for i in words if len(i) > 3])
print([i.upper() for i in words])
