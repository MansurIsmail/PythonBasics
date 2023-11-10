#   Making Numerical List

print("***** range(4, 10, 2) - start=4, stop=10, step=2 ********")
for num1 in range(4, 10, 2):
    print(f'number in this iteration: {num1}')

print("***** range(4, 10) - without step, default step=1 ********")
for num1 in range(4, 10):
    print(f'number in this iteration: {num1}')

print("***** range(10) - default start=0, step=1 ********")
for num1 in range(10):
    print(f'number in this iteration: {num1 + 0.8888888}')

print(f'data type of range function result: {type(range(10))}')
print('***** Creating the list from the range() result: *******')

nums1 = [range(10)]  # did not work
print(f"num1 list: {nums1}")
print(type(nums1))
# first element is the function itself not the result of the function
print(type(nums1[0]))

nums2 = list(range(10))
print(f"num2 list: {nums2}")

# Problem 1: print the squares of even numbers from 100 to 120(inclusively)

print("**** range (100, 121, 2) ****")
squares = []
for num1 in range(100, 121, 2):
    squares.append(num1 * num1)
print(f'Final list: {squares}')

nums = list(range(100, 121, 2))
for num in nums:
    print(num ** 2)

for num in range(100, 121, 2):
    print(f"printing squares of even numbers from 100 to 120 is {num} squares to {num ** 2} ")

print("***********************")
for num1 in range(10):
    print(f'***** outer loop: {num1} ******')
    for num2 in range(5):
        print(f'inner loop: {num2}')

print(" ********* Multiplication table 1-10: *************\n")
for num1 in range(1, 11):
    for num2 in range(1, 11):
        print(f'{num2} * {num1} = {num1 * num2}', end='\t\t')
    print()  # new line, so next print starts in a new line everytime num1 changes

print("\n******* find the max and min in the list.*********")
nums = [5, 0, 2, 25]
nums.sort()  # sorts in ascending ( lowest to highest)
min_num = nums[0]
max_num = nums[-1]
print("****** find the sum of list elements.********")
# pseudocode
# have new variable for sum=0
print(nums)
total = 0
# loop through the list then keep incrementing the sum by each element : sum = sum + num
for num in nums:
    print(f"***** current sum: {total} *****")
    print(f"current num: {num}")
    total = total + num
# after loop print the result
print(f"SUM: {total}")


# comprehension
cars = ['toyota', 'lexus', 'honda', 'bmw']
nums = [2, 3, 8, 29, 19]
# create list of squares, print the list
squares = []
for num in nums:
    squares.append(num**2)
print(squares)

# list comprehension - list and append in one line
cubes = [num**3 for num in nums]
print(cubes)

updated_cars = [car.upper() for car in cars]
print(updated_cars)
print(cars)
print(f"last car in the list {cars[-1]}.")


# H/W: 4-3 to 4-9
print('****** H/W 4-3 to 4-9 ********')
print('\n# 4-3')
for i in range(1,21):
    print(i)
print('\n# 4-4')
numbers = list(range(1, 1000001))
# for i in numbers:
 #   print(i)
print('\n# 4-5')
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print('\n# 4-6')
for i in range(1, 20, 2):
    print(i)
print('\n# 4-7')
for i in list(range(3, 31, 3)):
    print(i)
print('\n# 4-8')
c_s = []
for val in range(1, 11):
    c_s.append(val**3)
for i in c_s:
    print(i)


print("\n")
for i in list(range(1, 11)):
    print(i**3)

print('\n# 4-9')
cubs = [value**3 for value in range(1, 11)]
print(cubs)

