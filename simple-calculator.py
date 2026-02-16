#import tkinter 

decision = input("Hi, What would you like to use? (A. Calculator, B. Word Analysis Tool \nor Type 'e' to Exit): ")

def calc():
    if operation == "+":
        return input1+input2
        #addition = input1 + input2
        #return int(addition) if type(addition) is int else addition #this will never even work-?! stupid
    elif operation == "-":
        return input1 - input2
    elif operation == "*":
        return input1 * input2
    elif operation == "/":
        if input2 == 0:
            return "Error: Division by Zero"
        else:
            return input1/input2 #f"{result:.7f}" - this is silly because it makes 1.5 to 1.5000000
    else:
        return "Please input a valid operation"
    
def char_counter():
    word = input("Enter your word/sentence: ")
    joined_word = word.replace(" ","")
    count = 0
    for i in joined_word:
        count+=1
    print(f"There are {count} number of characters in the phrase \"{word}\"")

def palindrome():
    word = input("Enter your word: ")
    def pal(word):
        if word == "":
            return word
        else:
            return pal(word[1:]) + word[0]
    new_word = pal(word)
    if word == new_word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"






if decision == "A" or decision == "a":
    input1 = int(input("Enter your 1st number: "))
    operation = input("Enter your operator (+, -, *, /): ")
    input2 = int(input("Enter your 2nd number: "))
    print(f"{input1} {operation} {input2} = {calc()}")

elif decision == "B" or decision == "b":
    input3 = input("What tool would you like to use?\nA. Character Counter\nB. " \
    "Palindrome Checker\nC. Reverse a Word: ")
    if input3 == "A" or input3 == "a":
        char_counter()
    elif input3 == "B" or input3 == "b":
        print(palindrome())
    elif input3 == "C":
        pass
    else:
        print("Please enter a valid option")

elif decision == "e":
    print("See you soon!")

else:
    print("Please input a valid option")
