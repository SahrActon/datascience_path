# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer
# Please reference to Day1-Task_2-Data-types.py


# There are four collection data types in python programming language
"""
 List - is a collection which is
        - ordered and changeable.#
        - Allows duplicates members

 Tuple - is a collection which is
        - ordered and unchangeable.
        - allows duplicate members

 Set    - is a collection which is
        - unordered
        - un-indexed
        - No duplicate member
"""
# List
# Task 1 -
print("Task 1")
# it is ordered in the way that the data is entered
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
print(thisList)

# Task 2 -
print("Task 2")
# it is ordered in the way that the data is entered
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
print(thisList[2:5])

# Task 3 -
print("Task 3")
# it is ordered in the way that the data is entered
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
print(thisList[:4])

# Task 4 -
print("Task 4")
# it is ordered in the way that the data is entered
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
print(thisList[2:])

# Task 5 -
print("Task 5")
# it is ordered in the way that the data is entered
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
print(thisList[-6:-2])

# Task 6 -
print("Task 6")
# it is ordered in the way that the data is entered
# This example returns the items from index -4 (included) to index -1 (excluded)
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
thisList[1] = "apricot "
print(thisList)

# Task 7 -
print("Task 7")

for x in thisList:
    print(" ", x)

# Task 8 -
print("Task 8")
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
if "apple" in thisList:
    print("apple is in the list")

# Task 9 - checking the length
print("Task 9")
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
print(len(thisList))

# Task 10 - adding to the list
print("Task 10")
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
thisList.append("pear")
print(thisList)

# Task 11 - inserting at a specific position
print("Task 11")
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
thisList.insert(1, "pear")
print(thisList)

# Task 12 - remove an image from the list
print("Task 12")
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
thisList.remove("mango")
print(thisList)

# Task 13 - pop() method removes the specified index, (or the last item if index is not specified):
print("Task 13")
thisList = ["apple", "mango", "banana", "cherry", "orange", "kiwi", "mellon"]
thisList.pop()  # this will remove "mellon"
print(thisList)

# Task 14 -
print("Task 14")
thisList = ["apple", "mango", "banana", "cherry", "orange"]
del thisList[0]  # this will delete the object from the list index
print(thisList)

# Task 15 - delete everything from the list
print("Task 15")
thisList = ["apple", "mango", "banana", "cherry", "orange"]
del thisList
# print(thisList) # printing this will cause an error because the list has been deleted & doesn't exist

# Task 16 -  clearing the list
print("Task 16")
thisList = ["apple", "mango", "banana", "cherry", "orange"]
thisList.clear()  # this empties the list
print(thisList)

# Task 17 - copy
# if you want to copy a list use the copy function
# dont use = because this means that its a reference to the list
print("Task 17")
thisList = ["apple", "mango", "banana", "cherry", "orange"]
list2 = thisList.copy()
print(list2)

# Task 18 -
print("Task 18")
# another way to copy a list is to use the list() method
thisList = ["apple", "mango", "banana", "cherry", "fi"]
list3 = list(thisList)
del list3[-1]
print(list3)

# Task 19 - Join two lists using the "+" method
print("Task 19")
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]
list3 = list1 + list2

print(list3)

# Task 20 - append method of joining two list together
print("Task 20")
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

# Task 21 - using the extend method
print("Task 21")
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# Task 22 -
print("Task 22")
thelist = list(("apple", "orange", "banana"))
print(thelist)

# Task 23 -
print("Task 23")
thelist = list(("apple", "orange", "banana"))
thelist2 = list(("kiwi", "orange", "banana"))
thelist.append("hello")
print("Extra 1", thelist)

print("Extra 1.5", thelist.clear())

x = thelist2.copy()
print("Extra 2", x)

thelist = list(("apple", "orange", "banana"))
thelist2 = list(("kiwi", "orange", "banana"))
print("Extra 3", thelist.count("apple"))  # count how many times apple appears in the list

thelist.extend(thelist2)
print("Extra 4", thelist)

print("Extra 4.5", thelist.index("banana"))
thelist.insert(1, "hello")  # insert what we a word at a specific index
thelist.pop()  # remove the last word from the list
print("Extra 5", thelist)

thelist.remove("hello")
print("Extra 6", thelist)  # remove a word from the list

thelist.reverse()
print("Extra 7", thelist)  # .reverse the list back to front
thelist.sort()
print("Extra 8", thelist)
