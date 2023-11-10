guests = ['Sofiya', 'Akmal', 'Obama', 'Trump']

# for guest in guests: # this line sets the iteration, 4 times
#     print(f"You are still invited {guest}.")
#     guests.remove(guest)
#     print(f"current list: {guests}")
#     # removing the elements by value

# looping using index
# find how many elements in the list? len(guests)
# loop number of times as number of elements using range()
print('length: ', len(guests))
# for i in range(len(guests)):  # range(4) ; i = 0, 1, 2, 3
#     print(f'current index: {i}')
#     del guests[0]  # removing elements by index
#     print(f'new guests list: {guests}')

# remove last 2 from the list
# for i in range(2):  # range(2) ; i = 0, 1
#     print(f'current index: {i}')
#     del guests[-1]  # removing elements by index
#     print(f'new guests list: {guests}')
#
#
print(f"asdfasdfasdfasdf\n{guests}\nasdfasdfasdf")
print(f"asdfasdfasdfasdf\n{guests}\nasdfasdfasdf")
print(guests.sort())
print(guests.pop())

