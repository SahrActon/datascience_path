# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer
# Please reference to Day1-Task_2-Data-types.py

# Set is a collection which is unordered and unindexed. In pythons sets are written with curly brackets

# Task 1 -

print("Task 1")
thisSet = {"Apple", "Banana", "Cherry"}
print(thisSet)

# Task 2 - Accessing all of the items
print("Task 2")
thisSet = {"Apple", "Banana", "Cherry"}
for x in thisSet:
    print('\t', x)

# Task 3 - check if "Banana" is present in the set
print("Task 3")
thisSet = {"Apple", "Banana", "Cherry"}
print('\t', 'Banana' in thisSet)

# Task 4 - add items
print("Task 4")
thisSet = {"Apple", "Banana", "Cherry"}
thisSet.add("Melon")
print('\t', thisSet)

# Task 5 - add multiple to a set, using the update() method
print("Task 5")
thisSet = {"Apple", "Banana", "Cherry"}
thisSet.update(["Melon", "Orange", "Mango"])
print('\t', thisSet)

# Task 6 - Get the length a Set
print("Task 6")
thisSet = {"Apple", "Banana", "Cherry"}
print('\t', len(thisSet))

# Task 7 - remove()
print("Task 7")
thisSet = {"Apple", "Banana", "Cherry"}
thisSet.remove("Banana")
print('\t', thisSet)

# Task 8
print("Task 8")
thisSet = {"Apple", "Banana", "Cherry"}
thisSet.discard("Cherry")
print('\t', thisSet)

# Task 9
print("Task 9")
thisSet = {"Apple", "Banana", "Cherry"}
x = thisSet.pop()
print('\t', x)
print('\t', thisSet)

# Task 10
print("Task 10")
thisSet = {"Apple", "Banana", "Cherry"}
thisSet.clear()
print('\t', thisSet)

# Task 11
print("Task 11")
thisSet = {"Apple", "Banana", "Cherry"}
del thisSet
# print('\t', thisSet)  # this will raise an error

# Task 12 - Join two sets -
# # we can use union() method that returns a new set containing all items from both sets
# or the update() method that inserts all of the items from one into another

print("Task 12")
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
thisSet = set1.union(set2)
print('\t', thisSet)

# Task 13
print("Task 13")
set01 = {"a", "b", "c"}
set02 = {"1", "2", "3"}
set01.update(set02)
print('\t', set01)

# Task 14
print("Task 14")
thisset = set(("apple", "banana", "cherry"))
print('\t', thisSet)

# Task 15
print("Task 15")

# Task 16
print("Task 16")

# Task 17
print("Task 17")
