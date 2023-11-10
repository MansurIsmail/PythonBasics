# Functions , logical units of the code with certain purpose
# unique name with lower case (not shadowing built-in function)
# def name_of_the_function():
# indentation, that shows function block, code belongs to function
# 1. defining the function:
def hello():
    msg = f"Hello World function!"
    msg1 = f"second line"
    msg2 = f"third line"
    msg3 = f"fifth line"
    msg4 = "************************"
    final_msg = f"{msg}\n{msg1}\n{msg2}\n{msg3}\n{msg4}"


def hello_return():
    msg = f"Hello World function!"
    msg1 = f"second line"
    msg2 = f"third line"
    msg3 = f"fifth line"
    msg4 = "************************"
    final_msg = f"{msg}\n{msg1}\n{msg2}\n{msg3}\n{msg4}"
    return final_msg


def hello_name(name):  # name is the parameter (general)
    print(f"Hello World {name.title()}!")
    print(f"Thank you for joining")
    print("************************")


def addition(num1, num2):
    # print(f"Addition of {num1} and {num2} is {num1 + num2}")
    return num1 + num2


# 2. execute the function:
result_of_print = hello()
print(result_of_print)
print("---------------")
result_of_print2 = hello_return()
print(result_of_print2)
print("---------------")
hello_name("john")  # argument , specific value for the parameter
hello_name("jane")
print(f'addition: {addition(45, 65)}')
print(addition(45, 65))

print("Unit testing : executing the functions with various arguments and check with expected result")
print(addition(2, 3) == 5)
# print(addition(2, 'a') == "Error: enter integers not characters")
# print(addition(2, None) == "error: enter valid numbers")
# print(addition(-2, -100) == -102)

# print('addition of 1 and 5 is ' + 6)
print('addition of 1 and 5 is', 6)
print('addition of 1 and 5 is ' + str(6))
print(f'addition of 1 and 5 is {1+5}')
print(f'addition of 1 and 5 is {1+5}')


