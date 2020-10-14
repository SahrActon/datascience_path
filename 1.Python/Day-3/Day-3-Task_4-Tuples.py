# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer
# Please reference to Day1-Task_2-Data-types.py

# Tuples are unchangeable

print("Task 1")
thisTuple = ("apple", "banana", "cherry", "mango", "tomato", "kiwi")
print(thisTuple)

# Task 2 -
print("Task 2")
print(thisTuple[1])

# Task 3 -
print("Task 3")
print(thisTuple[-1])

# Task 4 -
print("Task 4")
print(thisTuple[2:5])

# Task 5 -
print("Task 5")
print(thisTuple[-4:-1])  # returns the items from index -4(included) to index -1 (excluded)

# Task 6 - Changing Tuple Values
'''

Once a tuple is created, you cannot change it values. Tuples are
    :* unchangeable *
    :* immutable *

1. You can convert the tuple into a list, 
2. Change it the list
3. Convert the list back into a tuple      

'''
print("Task 6")
x = ("Tom", "Tim", "Bob")
y = list(x)
y[1] = "new_name"
x = tuple(y)
print(x)

# Task 5
print("Task 5")
thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
    print("Apple is in the list")

# Task 6
print("Task 6")
thisTuple = ("apple", "banana", "cherry")
print(len(thisTuple))

# Task 7
# print("Task 7 this will raise an error")
thisTuple = ("apple", "banana", "cherry")
# thisTuple[3] = "orange"  # this will raise an error
# print(len(thisTuple))

# Task 8
print("Task 8")
nonTuple = ("apple")
print(type(nonTuple))
thisTuple = ("apple",)
print(type(thisTuple))

# Task 9 - deleting from tuple
print("Task 9 this will raise an error")
thisTuple = ("apple", "banana", "cherry")
del thisTuple
# print(thisTuple)  # this will raise an error

# Task 10 - Joining two tuples
print("Task 10")
tuple1 = ("a", "b")
tuple2 = ("c", "d")

tuple3 = tuple1 + tuple2
print(tuple3)

# Task 11 - Tuple constructor
print("Task 11")
thistuple = tuple(("apple", "banana"))
print(thistuple)

