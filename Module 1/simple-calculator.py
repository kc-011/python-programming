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
    word_list = []
    for i in word:
        if i.isalnum():
            word_list.append(i)
    edited_word = "".join(word_list)
    #print(edited_word) for debugging
    def pal(edited_word):
        if edited_word == "":
            return edited_word
        else:
            return pal(edited_word[1:]) + edited_word[0]
    new_word = pal(edited_word)
    #print(new_word) for debugging
    if edited_word.lower() == new_word.lower():
        return f"\"{word}\" is a palindrome"
    else:
        return f"\"{word}\" is not a palindrome"

def reverse():
    word = input("Enter your word/sentence: ")
    def rev(word):
        if word == "":
            return word
        else:
            return rev(word[1:]) + word[0]
    new_word = rev(word)
    return new_word



if decision == "A" or decision == "a":
    input1 = float(input("Enter your 1st number: "))
    operation = input("Enter your operator (+, -, *, /): ")
    input2 = float(input("Enter your 2nd number: "))
    print(f"{input1} {operation} {input2} = {calc()}")

elif decision == "B" or decision == "b":
    input3 = input("What tool would you like to use?\nA. Character Counter\nB. " \
    "Palindrome Checker\nC. Reverse a Word: ")
    if input3 == "A" or input3 == "a": 
        char_counter()
    elif input3 == "B" or input3 == "b":
        print(palindrome())
    elif input3 == "C" or input3 == "c":
        print(reverse())
    else:
        print("Please enter a valid option")

elif decision == "e":
    print("See you soon!")

else:
    print("Please input a valid option")

"""
2 things I'm not happy with:
a) int/float user input in calculator - I want 3*4 to be 12 and not 12.0, but if I do int(input)
then I cannot input a float, the calculator will use only whole numbers ?!?!

Solution - It really doesn't matter. I changed it to 'float(input...)'. That stuff matters if you
need to display it somewhere (frontend)

b) I want the user input to repeat, once a task is complete, the main question "What would
 you like to use? (A. Calculator...." should be asked again instead of pressing the run button 
 repeatedly. to close the program, the user can input "e". tried this using while loop (even searched
 it up) but not working

"""