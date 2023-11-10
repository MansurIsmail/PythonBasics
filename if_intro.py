countries = ['uSa', 'cAnada', 'France', 'uK']
nums = []
if nums:
    print("nums is not empty")
else:
    print("nums is empty")

for country in countries:
    if country.lower() == 'usa':  # make the variable lower case to compare with lower case 'usa'
        # following line is executed when country == 'usa' expression returns True
        print(country.upper())
    else:
        # in all other cases
        print(country.title())

# Expressions you can use in if statement
# False: 0, empty list, empty dictionary
# a == b
# a >= b , example: num >= 456, num <= 456
# a != b , example: num ! = 0
# a > b , example:  num > 22, num < 22
# value in list_name , example: 'usa' in countries, 34 in nums

# combination of conditions using operator : OR, AND
# a == b or a == c : either a is equal to b or a is equal to c
# True or True => True
# True or False => True
# False or True => True
# False or False => False

# a == b and a == c : a is equal to b and c (a <= b <= c)
# a == b and d == c : a is equal to b and d is equal to c (independent conditions)
# True and True => True
# True and False => False
# False and True => False
# False and False => False

b = 10
a = 10  # assigning the value 10 to a variable "a"
print(a == b)  # comparing the value of 'a' variable to value of 'b' variable

print("---------------------")
# age = 25
age = int(input("enter your age: "))
if age < 17:
    print(f"You are not eligible, but you can apply for driving licence after {17 - age} year(s).")
elif 17 < age < 25:
    print(f"You are eligible to apply for DL for junior.")
else:
    print("You are eligible to apply for driving licence.")

print("============================")
nums = [45, 4, 566, 88, 1, 0]
# print I found it when 88 is in the list
num = input("enter the number to check: ")  # string
print('number from the input:', num)
print(type(num))
# num = int(num)
if int(num) in nums:
    print("I found it in my list")

# '88' is not the same as 88
# H/W : 5-5, from 5-6 to 5-11
# FuzzBuzz :
# pass a number as input. convert to int
# if num is dividable by 3 print Fuzz
# if num is dividable by 5 print Buzz
# if num is dividable by 3 and 5 print FuzzBuzz
nom = int(input('Enter the nom to check: '))
if nom % 3 == 0 | nom % 5 == 0:  # or nom % 15 == 0
    print('FuzzBuzz')
elif nom % 5 == 0:
    print('Buzz')
elif nom % 3 == 0:
    print('Fuzz')
else:
    print('Today is not your day!')













