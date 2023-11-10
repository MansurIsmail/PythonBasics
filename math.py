"""
Write a Python function that accepts three parameters.
The first parameter is an integer.
The second is one of the following mathematical operators: +, -, /, or .
The third parameter will also be an integer.
The function should perform a calculation and return the results.
For example, if the function is passed 6 and 4, it should return 24.
calculate(6, "/", 4) -> 24

def calculator(number1, operator, number2):
    # code here

remember :  return "Oops! Can't divide by zero. "
and if operator is invalid return "Invalid operator. Try +, -, *, or /."
"""

def calculator(number1, operators, number2):
    if operators == '/':
        if number2 == 0:
            return "Oops! Can't divide by zero."
        return number1 / number2
    elif operators == '+':
        return number1 + number2
    elif operators == '-':
        return number1 - number2
    elif operators == '*':
        return number1 * number2
    else:
        return "Invalid operator. Try +, -, *, or /."

number1 = int(input("enter number1: "))
operators = input("enter math symbol: ")
number2 = int(input("enter number2: "))
print(calculator(number1, operators, number2))

for i in range(5):
    print(f"Case #{i+1}")
    number1 = int(input("enter number1: "))
    operators = input("enter math symbol: ")
    number2 = int(input("enter number2: "))
    print(calculator(number1, operators, number2))
    calculator(number1, operators, number2)

def calculator(number1, oprtr, number2):
    if oprtr == '/':
        if number2 != 0:
            print(number1 / number2)
        else:
            print("Oops! Can't divide by zero.")
    elif oprtr == '+':
        print(number1 + number2)
    elif oprtr == '-':
        print(number1 - number2)
    elif oprtr == '*':
        print(number1 * number2)
    else:
        print("Invalid operator. Try +, -, *, or /.")

for i in range(5):
    print(f"Case #{i+1}")
    number1 = int(input("enter number1: "))
    oprtr = input("enter math symbol: ")
    number2 = int(input("enter number2: "))
    print(calculator(number1, oprtr, number2))


# new coment to submit to GIT