
input1 = float(input("Enter your 1st number: "))
operation = input("Enter your operator (+, -, *, /): ")
input2 = float(input("Enter your 2nd number: "))

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

print(f"{input1} {operation} {input2} = {calc()}")