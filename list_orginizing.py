# List is unorganized list, to organize we use sorting functions ('Order by' in SQL)
# permanently and temporary
cars = ['tesla', 'ferrari', 'bmw', 'lexus']
print(f"Original list: {cars}")
# permanent sorting will be done with sort(), asc is default order
cars.sort()  # asc order
print(f"Sorted list: {cars}")
cars.append('lambo')
print(f"Updated list: {cars}")
# we want to order in desc order
cars.sort(reverse=True)
print(f"Sorted list in desc order: {cars}")

print("### temp sorting is done with sorted() ###")
cars_models = ['modelX', 'LaFerrari', 'series7', 'ES350']
print(f"Original list: {cars_models}")
# print(f'Sorted list: {sorted(cars_models)}')
print(f'Sorted list: {sorted(cars_models)}')
print(f"list after sorting: {cars_models}")
car_models_asc = sorted(cars_models)  # new list created, sorted car_models assigned
print(f'Sorted list: {car_models_asc}')
print(f"list after sorting asc: {cars_models}")

car_models_desc = sorted(cars_models, reverse=True)
print(f'Sorted list in desc order: {car_models_desc}')
print(f"list after sorting desc: {cars_models}")

# len() in python -> in java length() -> returns/shows number of items in the list
print(f"I have {len(cars)} cars in the garage.")
# last index is len(list)-1

print("###### reverse() - reverse without sorting #####################")
names = ['john', 'mark', 'jane', 'alex']
print(f"original list: {names}")
names.reverse()
print(f"after reverse list: {names}")


for i in range(100, 121, 2):
    print(f"even num from 100 to 121 is {i} and square of {i}: {i**2}")
# square w**2
print('\n******* H/W: 3-8, 3-10 *******')
print('\n**** H/W 3-8 ****')
print('***** Locations I would like to visit ******')
locations = ['Mecca', 'Munawara', 'Palestine', 'Istanbul', 'Kair']
print(f"{locations}")
print(f"\nPrinted with sorted() order: {sorted(locations)}.")
print(f"Printed in original order: {locations}.")
locations.reverse()
print('Reversed list ' + str(locations))
locations.reverse()
print(f"Reversed 2nd time list: {locations}.")
locations.sort()
print(f"After sort() asc order: {locations}.")
locations.sort(reverse=True)
print(f"After sort() desc order: {locations}.")
print('\n***** H/W 3-10 *****')
mountains = ['Kavkaz', 'Tibet', 'Alpy', 'Pamir', 'Andy']
print(mountains)
print(sorted(mountains))
print(sorted(mountains,reverse=True))
mountains.reverse()
print(mountains)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
print(f"My mounains: {len(mountains)}.")
