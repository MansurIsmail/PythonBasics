# Homework 4-10 to 4-15

print('--------- 4-10 --------')
"""
 4-10. Slices: Using one of the programs you wrote in this chapter, add several
 lines to the end of the program that do the following:
 • Print the message, The first three items in the list are:. Then use a slice to
 print the first three items from that program’s list.
 • Print the message, Three items from the middle of the list are:. Use a slice
 to print three items from the middle of the list.
 • Print the message, The last three items in the list are:. Use a slice to print
 the last three items in the list.
"""
my_cars = ['mercedes', 'audi', 'bmw', 'jeep', 'gmc', 'ram']
print(my_cars)
print(f"The first three items in the list are: {my_cars[:3]}.")
print(f"Three items from the middle of the list are: {my_cars[1:4]}.")
print(f"The last three items in the list are: {my_cars[3:]}.")


print('\n--------- 4-11 --------')
"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.
"""
pizzas = ['cheese', 'chiken', 'beef', 'pepperoni', 'veggi']
print(f"The original list: {pizzas}")
friend_pizzas = pizzas[:]
print(f"The copy of list: {friend_pizzas}")
pizzas.append('phily')
print(f"Added a new pizza to the original list: {pizzas}")
friend_pizzas.append('meat')
print(f"Added a different pizza to the list friend_pizzas: {friend_pizzas}")
for i in pizzas:
    print(f"My favorite pizzas are: {i.title()}")

for i in friend_pizzas:
    print(f"My friend’s favorite pizzas are: {i.title()}")


print('\n------ 4-12 -------')
"""
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
for i in my_foods:
    print(f"My favorite foods are: {i}")

for i in friend_foods:
    print(f"My friend's favorite foods are: {i}")


print('\n------ 4-13 -------')
"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
"""
foods = ('sandwich', 'burger', 'steak', 'bread', 'cheese')
for i in foods:
    print(f"Menu: {i}")
# foods[0]='hash'
foods = ('sandwich', 'hamburger', 'phily-steak', 'bread', 'cheese')
for i in foods:
    print(f"Updated Menu: {i}")







