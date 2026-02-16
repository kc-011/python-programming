#SLICING
#already know, but let's start from the basics and increase the difficulty
# and attempt every possible combination

word = "Python is great"
print(word[:5]) #index is not inclusive
print(word[5:6])
print(word[6:])
print(word[::-1])
print(word[-2:-5:-1])
print(word[-2:-5:])
print(word[-5:2:-1])
print(word[::3])
print(word[-1:-9:-1][::-2]) #can add more if needed
print(word[8:0:-3][::-2]) #[::] and [:0:] is not the same
print(word[1:len(word)-1])

#String Functions
#Strings are IMMUTABLE which is why we need to make a new string everytime we use a function 
# or just print the new thing without assigning

string = "  KaranChawla  "

print(string.upper())
print(string.lower())

#default is whitespace. can use for other characters as well
fruit = "-banana+."
print(fruit.rstrip("."))
print(fruit.lstrip("-"))
print(fruit.strip("-.+"))

#split func default sep is whitespace
#split gives a list of N+1 elements if you have an 'N' separator
#split also gives you empty strings as an element if the separator is:
# In the beginning of the string
# At the end of the string
# If 2 or more separators are consecutively there 
print(string.split(sep='a'))
print("a banana".split(sep="a"))

#title func capitalizes first letter of each word
book = "the last polar bear"
print(book.title())

#find func returns index of letter given (first find), returns -1 if not found
print(book.find("r"))

#replace func replaces all instances of old letter with new string
print(book.replace("l","💙"))
print(book.replace("ar","🆖"))

#format func, lowkey useless?
#f strings are better and preferred
#used in dynamic programming - when you have the template only
# or in older versions of python
s = "I have {}. Enough for only {} people"
print(s.format("cake", 25))

str = "Today'S HOme WoRk iS abOuT SeparAtIng 12345 from chAraCterS"

lower_case_letters = []

upper_case_letters = []

digits = []

characters = []

for i in str:
    if i.islower():
        lower_case_letters.append(i)
    elif i.isupper():
        upper_case_letters.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        characters.append(i)
print(lower_case_letters)
print(upper_case_letters)
print(digits)
print(characters)

#other things we can check:
"""
s.isalpha()
s.isalnum()
s.isspace()
s.startswith("abc")
s.endswith("xyz")

"""

new_word = word.split()
print(new_word)
#join func to join a list of words with character of choice into a string
new_word = "-".join(new_word)
print(new_word)

#we can also chain functions together
print(word.strip().upper().replace(" ", "_"))

#count func 
print(word.count("t"))

#index func - similar to find but returns error instead if char not found
print(word.index("o"))

#swapcase func flips the case(upper/lower) of the letters
print(string.swapcase())

#partition func separates the string into exactly 3 parts, storing them
# in a tuple. first occurence is taken
print(word.partition("gr"))