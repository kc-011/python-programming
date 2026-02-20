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
#Create a list of word lengths.
#Create a list of words with length > 3.
#Create a list of uppercase words.
print([len(i) for i in words])
print([i for i in words if len(i) > 3])
print([i.upper() for i in words])

#Create a 3x3 matrix filled with 1s
print([[1 for i in range(3)] for i in range(3)])

#Flatten this list into [1,2,3,4,5,6]
matrix = [[1,2],[3,4],[5,6]]
print([j for i in matrix for j in i])

#Create multiplication table pairs
print([(i,j) for i in range(1,4) for j in range (1,4)])

#Classic FizzBuzz Problem
print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1,21)])

#Flatten this list:
cube = [[[1,2],[3,4]], [[5,6],[7,8]]]
print([k for i in cube for j in i for k in j])

#print (i,j) only if i!=j
#filtering:
print([(i,j) for i in range(1,6) for j in range (1,6) if i!=j])
#replacing:
print([(i,j) if i!=j else ("$","$") for i in range (1,6) for j in range(1,6)])

