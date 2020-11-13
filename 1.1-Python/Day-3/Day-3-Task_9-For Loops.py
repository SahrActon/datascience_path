# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7

# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7

print("Task 1 -")
# Task 1 -
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break  # break out of our for loop
    print(num)

print('\n')
# ------------------------------------------------------------------------------------------------------------------

for num in nums:
    # continue
    if num == 3:
        print('Found')
        continue  # continue our for loop
    print(num)

print('\n')
# ------------------------------------------------------------------------------------------------------------------
# Task 2 - Nested loop
print("Task 2 -")
for num in nums:
    for letter in 'abc':
        print(num, letter)

print('\n')
# ------------------------------------------------------------------------------------------------------------------
# Task 3 - range
print("Task 3 -")
for i in range(10):
    print(i)

print("\nRange starting from 1 and ends at 10(not including")
for i in range(1, 10):
    print(i)
print('\n')
# ------------------------------------------------------------------------------------------------------------------

# source - https://www.w3schools.com/python/python_for_loops.asp


# Task 4 - loop through a list
print("Task 4 -")
fruits = ["apple", "banana", "cherry"]  # list
for fruit in fruits:
    print(fruit)
print('\n')

# Task 5 - looping through letters
print("Task 5 -")
for letter in "banana":
    print(letter)
print('\n')

# Task 6 -
print("Task 6 -")
fruits = ["apple", "banana", "cherry"]  # list
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        print("we have found the fruit we will no exit")
        break
print('\n')

# Task 7 - exit the loop when 'x' is 'banana', but this time the break comes before the print:
print("Task 7 -")
fruits = ["apple", "banana", "cherry"]  # list
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        print("we have found the fruit, but we will continue looping")
        break
    print(fruit)
print('\n')

# Task 8 -
print("Task 8 -")
fruits = ["apple", "banana", "cherry"]  # list
for fruit in fruits:
    if fruit == "banana":
        print("we found banana")
        continue
    print(fruit)
print('\n')

# Task 9 -
print("Task 9 -")
for i in range(9):
    print(i)

print('\n')

for i in range(2, 6):
    print(i)

print('\n')

# The range() function defaults to increment the sequence by 1, however it
# is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for i in range(2, 40, 2):
    print(i)
print('\n')

# Task 10 - Else
# The else statement in a for loop specifies a block of code that will be executed when the loop is finished
print("Task 10 - Else")
for x in range(6):
    print(x)
else:
    print("Finally finished")
print('\n')

# Task 11 - nest for loop
print("Task 11 - Nested Loop")
words = ['red', 'big', 'tasty']
fruits = ["apple", "banana", "cherry"]  # list
for word in words:
    for fruits in fruits:
        print(word, fruit)
print('\n')

# Task 12 - pass
print("Task 12")
for x in [0, 1, 2, 3, 4]:
    pass
