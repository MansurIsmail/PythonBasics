#  Homework 5-1 to 5-15

print('------ 5-1 ------')
"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this: look example.
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
car = 'honda'
print("Is car == 'honda'? I predict True.")
print(car == 'honda')

print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')
cars = ['toyota', 'honda', 'suzuki', 'lexus', 'akura']
for i in range(10):
    print(f"\ncase#{i+1}")
    c = input("Enter car to check: ")
    print("Car from input", c )
    if c.lower() in cars:
        print(f"Car is in list. Result: {c == c}")
    else:
        print(f"Car is not in cars list. Result: {c != c}")

# Automated version
print('\n-----Automation of code -----')
cars = ['toyota', 'honda', 'suzuki', 'lexus', 'akura']
autos = ['bmw', 'mercedes', 'audi', 'wolswagen', 'porshe']

for i in cars:
    if i in cars:
        print(f"Car is in list. Result: {True}")
else:
    for i in autos:
        print(f"Car is not in cars list. Result: {False}")


print('\n------- 5-2 -------')
"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

car = 'honda'
print('Car is', car)
print(f"Is car equal 'Honda'? Result: {car.lower().upper().title() == 'Honda'}")
print(f"Is car equal 'toyota'? Result: {car.lower().upper().title() == 'toyota'}")

age = 20
print('Age is', age)
print(f"Is age = 20? Result: {age == 20}")
print(f"Is age = 1? Result: {age == 1}")
print(f"Is 0<age<25? Result: {0<age<25}")
print(f"Is 0>age>25? Result: {0>age>25}")
print(f"Is 0<=age<=20? Result: {0<=age<=20}")
print(f"Is 22<=age<=12? Result: {22<=age<=12}")

print(f"Is car=honda and age=20? Result:{car == 'honda' and age == 20}")
print(f"Is car=toyota and age=30? Result:{car == 'toyota' and age == 30}")
print(f"Is car=honda or age=30? Result:{car == 'honda' or age == 30}")
print(f"Is car=toyota or age=30? Result:{car == 'toyota' or age == 30}")

cars = ['bmw', 'gmc', 'ram']
print(cars)

c = input()
if c.title().upper().lower() in cars:
    print('Car is in list!')
else:
    print('Sorry we do not have it!')

print('\n------- 5-3 --------')
"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•	 Write an if statement to test whether the alien’s color is green. If it is, print 
a message that the player just earned 5 points.
•	 Write one version of this program that passes the if test and another that 
fails. (The version that fails will have no output.)

"""
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('The player just earned 5 points!')
if 'blue' in alien_color:
    print('The player just earned 5 points!')


print('\n------ 5-4 -------')
"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
write an if-else chain.
•	 If the alien’s color is green, print a statement that the player just earned 
5 points for shooting the alien.
•	 If the alien’s color isn’t green, print a statement that the player just earned 
10 points.
•	 Write one version of this program that runs the if block and another that 
runs the else block
"""
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('The player just earned 5 points for shooting the alien !')
if 'gray' not in alien_color:
    print('The player just earned 10 points.')

if 'green' not in alien_color:
    print('The player just earned 10 points.')
else:
    print('The player just earned 5 points for shooting the alien !')

print('\n------ 5-5 ------')
"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
•	 If the alien is green, print a message that the player earned 5 points.
•	 If the alien is yellow, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 15 points.
•	 Write three versions of this program, making sure each message is printed 
for the appropriate color alien.
"""
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print('The player just earned 5 points.')
elif 'yellow' in alien_color:
    print('The player just earned 10 points.')
elif 'red' in alien_color:
    print('The player just earned 15 points.')

if 'yellow' in alien_color:
    print('The player just earned 10 points.')
elif 'green' in alien_color:
    print('The player just earned 5 points.')
elif 'red' in alien_color:
    print('The player just earned 15 points.')

if 'red' in alien_color:
    print('The player just earned 15 points.')
elif 'yellow' in alien_color:
    print('The player just earned 10 points.')
elif 'green' in alien_color:
    print('The player just earned 5 points.')

print('\n------ 5-6 ------')
"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an
elder.
"""

age = 16
if age<2:
    print('the person is a baby.')
elif 2<=age<4:
    print('the person is a toddler.')
elif 4<=age<13:
    print('the person is a kid.')
elif 13<=age<20:
    print('the person is a teenager.')
elif 20<=age<65:
    print('the person is an adult.')
else:
    print('the person is an elder.')

print('\n------ 5-7 ------')
"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list.
•	 Make a list of your three favorite fruits and call it favorite_fruits.
•	 Write five if statements. Each should check whether a certain kind of fruit 
is in your list. If the fruit is in your list, the if block should print a statement, 
such as You really like bananas
"""
favorite_fruits = ['apple', 'banana', 'peach']
if 'apple' in favorite_fruits:
    print('You really like apple')
if 'banana' in favorite_fruits:
    print('You really like banana')
if 'peach' in favorite_fruits:
    print('You really like peach')
if 'fruit' in favorite_fruits:
    print('You really like fruit')
if 'pear' in favorite_fruits:
    print('You really like pear')

print('\n------ 5-8 ------')
"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for loging in again.
"""
usernames = ['admin', 'riberro', 'jonh', 'maga', 'gaga']
for i in usernames:
    if i == 'admin':
        print('Hello, ' + i + ', would you like to see a status report?')
    else:
        print('Hello,', i + ', thank you for loging in again.')

print('\n------ 5-9 ------')
"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct 
message is printed.
"""
users = []
if users:
    for i in users:
        print(f"Hello, {i}!")
else:
    print('We need to find some users!')

print('\n------ 5-10 ------')
"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted
"""
current_users = ['admin', 'riberro', 'jonh', 'maga', 'gaga']
new_users = ['toyota', 'riberro', 'Jonh', 'lexus', 'gaga']
for i in new_users:
    if i.lower() in current_users:
        print('the person will need to enter a new username.')
    else:
        print('the username is available.')

print('\n------ 5-11 ------')
"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line
"""
numbers = list(range(1,10))
print(numbers)
for i in numbers:
    if i == 1:
        print(f"{i}th\n")
    elif i ==2:
        print(f"{i}nd\n")
    elif i == 3:
        print(f"{i}rd\n")
    else:
        print(f"{i}th\n")




