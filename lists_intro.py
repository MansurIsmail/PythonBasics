# Data structures in Python

# List (Array), Dictionary (HashMap), Sets, Tuples
# For each DS we will learn:
# 1. CRUD operations (Create, Read (access the elements), Update (modifying the DS), Delete (elements))
# 2. Loop through the elements

#  List - collection of items, comma separated, covered with [] (in java {} )
print("****** (C) Creating the list *****************")
nums = [4, 2, 90, 33, 5]
print(nums)
print("Type of the variable: ", type(nums))
# creating the empty list
city_names = []  # in java it would be cityNames = {};
friends = list()  # list() function
print(city_names)
print(friends)

print("***** (R) Accessing the elements of the list: **************")
print('first element of nums list:', nums[0])
print('first element of nums list:', nums[-5])
print('last element of nums list:', nums[4])
print('last element of nums list:', nums[-1])
print('third element of nums list:', nums[2])

print("****** (U) Updating, Modifying the elements. ***************")
countries = ['usa', 'uk', 'canada', 'mexico']
print(countries)
countries[1] = 'spain'
print('after the change:', countries)
print("**** adding elements to the list using append(), insert() functions: ")
countries.append('italy')
print('after appending the value to the end of the list:', countries)
countries.insert(1, 'france')
print('after inserting the value to the beginning  of the list:', countries)

print("****** (D) Delete-Removing the elements from the list. ***************")
del countries[2]  # delete the element with index 2
print('after deleting the "spain" from the list:', countries)

deleted_countries = []
deleted_country1 = countries.pop()  # by default pop uses last index (-1), this means deletes last element
deleted_countries.append(deleted_country1)
print('after using pop() on the list:', countries)
print('deleted country: ', deleted_country1)
print("list of deleted countries:", deleted_countries)

# deleted_country2 = countries.pop(1)  # by default pop uses last index (-1), this means deletes last element
# deleted_countries.append(deleted_country2)
# print('deleted country: ', deleted_country2)
print('after using pop(1) on the list:', countries)
deleted_countries.append(countries.pop(1))
# 1. countries.pop(1) -> executed removes the france, and return the france
# 2. deleted_countries.append('france') -> appends the 'frane' to deleted_countries list
print("list of deleted countries:", deleted_countries)

print("**** removing the elements by value ******")
countries.append('canada')
print(countries)
# remove() - removes the first occurrence of the value, first canada in the list will be removed
abc = countries.remove('canada')
print("Final list of countries:", countries)
print(abc)  # None, since remove() function does not return anything, abc variable was not assigned anything

print('\n***** H/W: 3-4, 3-5, 3-6, 3-7, 3-9 *****')
guests = ['Obama', 'Bush', 'Truman', 'Putin', 'Ramazan']
print(guests)
print('****** New list has created ******')
print(f"{guests[0]}, we are inviting you for dinner, next Friday!")
print(f"{guests[1]}, we are inviting you for dinner, next Friday!")
print(f"{guests[2]}, we are inviting you for dinner, next Friday!")
print(f"{guests[3]}, we are inviting you for dinner, next Friday!")
print(f"{guests[4]}, we are inviting you for dinner, next Friday!")
print('******** Updating a list *********')
print("Truman is not able to come, we need to replace him with new guest.")
guests[2] = 'Mansur'
print('**** Mansur is new guest ****')
print(f"{guests[0]}, we are inviting you for dinner, next Friday!")
print(f"{guests[1]}, we are inviting you for dinner, next Friday!")
print(f"{guests[2]}, we are inviting you for dinner, next Friday!")
print(f"{guests[3]}, we are inviting you for dinner, next Friday!")
print(f"{guests[4]}, we are inviting you for dinner, next Friday!")
print('******* The table is expended ! *******')
guests.insert(0,'Deni')
guests.insert(2,'Faysal')
guests.append('Jack')
print(guests)
print('****** New invitation *******')
for i in guests:
    print(f"{i}, we are inviting you for dinner, next Friday!")

print('****** I can only invite two people ******')
print(guests)
print(f"I'm sorry we cannot invite you, {guests.pop()}.")
print(guests)
print(f"I'm sorry we cannot invite you, {guests.pop()}.")
print(guests)
print(f"I'm sorry we cannot invite you, {guests.pop()}.")
print(guests)
print(f"I'm sorry we cannot invite you, {guests.pop()}.")
print(guests)
print(f"I'm sorry we cannot invite you, {guests.pop()}.")
print(guests)
print(f"I'm sorry we cannot invite you, {guests.pop()}.")
print(guests)
for i in guests:
    print(f"You are still invited {i}.")
del guests[0]
del guests[0]
print(f'\n{guests}')


print('\n***** H/W 3-9 ****')
print(len(guests))





