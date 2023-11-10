# list - DS, iterable object, object with multiple items(elements) in it
# For loop - Looping allows you to take the same action, or set of actions, with every item in a list.

cars = ['tesla', 'ferrari', 'bmw', 'lexus']

# for varForEachIteration in nameOfTheList:
#     code to repeat
print("*******************")
# if you have 4 items in the list, for loop iterates 4 times, code in for loop is repeated 4 times
for car in cars:
    print(f"I like my {car.title()}.")  # this line is part of for loop block
    print("--------")   # repeated
print("These are all my cars ...")   # outside of loop, not repeated

guests = ['Sofiya', 'Akmal', 'Obama', 'Trump']
for guest in guests:
    pass  # do nothing
    print(f"{guest}, we are inviting you for the dinner, next Friday.")

# scope of the 'guest' variable is within for block (inside the loop)
# nested for loop
print('\n****** H/W: 4-1, 4-2 *******')
pizzas = ['cheese', 'chiken', 'beef', 'pepperoni', 'veggi']
for i in pizzas:
    print(i.title())

for i in pizzas:
    print('I like ' + i.title() + ' pizaa!')
print(f"I like the {pizzas[2].title()} and {pizzas[0].title()} pizzas so much! And I really love pizza!\n")
animals = ['dog', 'cat', 'horse']
print(animals)
for i in animals:
    print(f"A {i} would make a great pet.")
print(f"Any of these {animals} would make a great pet!")





