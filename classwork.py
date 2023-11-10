# This is the comment line - non-executable line; ignored by interpreter
# echo in linux , print in python, it prints the text in STDOUT
# print is the function in python (method)
# "Hello, World!" - is a string (text)
# print('Hello, World!')
import math

"""
This is the multi line comments, usually used for documentation in python
Possible error you might face when you start coding:
SyntaxError: when you code is written wrong way, check the symbols used, ", (),
NameError: when you type incorrect function name, string is not closed, not covered with quote (" ")
python is sensitive for the spaces in the beginning of the line, in python they are called Indentation
IndentationError: unexpected indent
"""

# variable - storage for values (complex values, file content, simple value etc) which can be reused by var name
# primitive data types: numbers (int, float), text (string), boolean (1/0 or True/False)
message = "I am variable value and can be changed. 45666666"
num1 = 25  # creating the variable, defining the variable and assigning the value to it
num2 = 30.45  # float
status = True  # boolean value, not 'true' or not 'TRUE', if False

print(message)
print(
    'Second time using the message value: ' + message)  # you can concatenate variable with text when variable value is a string
# print("Data type of the message variable: " + type(message)) # TypeError: can only concatenate str (not "type") to str
print("Data type of the message variable:", type(message))
print("Data type of the num1 variable:", type(num1))
print("Data type of the num2 variable:", type(num2))
print("Data type of the status variable:", type(status))

print(
    "Value of the num1 variable: " + str(num1))  # here str() function converts int to string, then concatenates strings
print("Value of the num1 variable:", num1)  # here print() function converts int to string
print("Value of the num2 variable:", num2)
print("Value of the status variable:", status)

# fstring - format-string
print(f"Value of the num1 variable: '{num1}'    .")
print(f"num1 multiplied by 50: '{num1 * 50}'    .")

# num3 = "num1 multiplied by 50: " + str(num1 * 50) + " more text at the end."  # without fstring
num3 = f"num1 multiplied by 50: {num1 * 50} more text at the end."  # text
print(num3)

####### Working with String values #####
## functions like title(), upper(), lower() are for string variables
print(message)
print(message.title())  # result: I Am Variable Value And Can Be Changed. 45666666,
print(message.upper())  # result: I AM VARIABLE VALUE AND CAN BE CHANGED. 45666666
print(message.lower())  # result: i am variable value and can be changed. 45666666
print(message)

msg2 = '   python  '
print(msg2)
print(msg2.strip('n'))
comment_string = '#....... Section 3.2.1 Issue #32 .......'
print(comment_string)
print(comment_string.strip('.#! '))  # 'Section 3.2.1 Issue #32'
print('www.example.com'.strip('wcom.'))  # example

num4 = '25'  # string (text) not an integer or float
# print(num4 + 10)  # TypeError: can only concatenate str (not "int") to str
print(int(num4) + 10)  # use int() function to convert num4 to int
print(float(num4) + 10)

print(f"Result: {num4} + 10.")

print("########## Mathematical operations +, -, *, /   ################")
num1 = 22
num2 = 4
print(f"Numbers we have: num1 = {num1} and num2 = {num2}")
print(f"Addition of numbers: {num1 + num2}")
print(f"Subtraction of numbers: {num1 - num2}")
print(f"Multiplication of numbers: {num1 * num2}")
print(f"Division of numbers: {num1 / num2}")
print(f"Division of numbers (rounded value): {round(num1 / num2, 1)}")

print("******** # in Python: // (floor division), % (modulo) ********")
print(f"Floor division of numbers: {num1 // num2}")
print(f"Modulo of numbers: {num1 % num2}")

print(f"Division of numbers then using floor(): {math.floor(num1 / num2)}")
print(f"Using the floor() function: {math.floor(456.78979)}")

# H/W : 2-8, 2-9, 2-10