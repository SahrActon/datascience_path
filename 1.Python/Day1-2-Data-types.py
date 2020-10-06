# Built-in Data Types
"""
These are the different data types built-in by default

Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
mapping types: dic
set types: set, frozenset
boolean types: bool
binary types: bytes, bytearray, memoryview
"""

# Exercise 1
print("Exercise 1")
x = 5
print(type(x))

# Exercise 2
print("\nExercise 2")

x_string = "Hello world"
print("String:", x_string, '\n')

x_int = 26
print("Int:", x_int, '\n')

x_float = 26.5
print("Float:", x_float, '\n')

x_complex = 1j
print("complex:", x_complex, '\n')

# ------------------------------------------------------------------------

# Exercise 3 - Working with list
print("\nExercise 3")
# resource used -> https://www.youtube.com/watch?v=W8KRzm-HUcc&ab_channel=CoreySchafer
# list
print("Working with list")
courses = ["ComSci", "Maths", "AI", "CivilEng", "Black History"]
print("All of the courses that we have", courses)
print("Getting the third index", courses[2])
print("Getting the last index", courses[-1])  # this is great way of getting the last index

# get the index from "0" up to but not include "2"
print("Getting a range of index", courses[0:2])

# Not include a value at the beginning [:2] instead of [0:2],
# python will assume that you want to get everything from the beginning up to but not including 2
print("Getting a range of index", courses[:2])

# Not include a value at the end [2:] instead of [2:5],
# python will assume that you want to get everything from the index to the end
print("Getting a range of index", courses[2:])

print("Getting the total length of courses", len(courses))

# ------------------------------------------------------------------------
# adding an item to our list
courses.append("Art")
print("We have now added art", courses)

# inserting to a specific index within the list
courses.insert(0, "Electronic Engineering")
print("We have now added Electronic Engineering at the beginning of our list", courses)

# insert using extend
additional_list = ["Wollof", "Economics"]
courses.extend(additional_list)
print("We have now added more courses ", courses)

# ------------------------------------------------------------------------
# Removing
courses.remove("Wollof")
print("We have now removed  Wollof ", courses)

popped = courses.pop()
print("Our popped item was ", popped)
print("We have now removed  the last item ", courses)

# ------------------------------------------------------------------------
# Other methods
# we want to reverse our list
courses.reverse()
print("We have now reversed the list", courses)

# we want to reverse our list
# courses.sort()
sorted_courses = sorted(courses)
print("We have now sored the list alphabetically ", sorted_courses)

# trying to find the index for a given string
print("The index of the string that you are looking for is localed at index: ", courses.index("AI"), '\n')

# Checking if value exist in list
print("Art" in courses)  # this should bring back true

# Turn our list in to comma separated vaules

courses_str = ", ".join(courses)
print(courses_str)

courses_str_2 = " - ".join(courses)
print(courses_str_2)

new_list = courses_str_2.split(" - ")
print("This is the new list ", new_list)
# ------------------------------------------------------------------------

# Working with numbers
nums = [1, 4, 2, 9, 10, 3]
print(nums)
nums.sort()  # ascending order
print("numbers sorted", nums)

nums.sort(reverse=True)  # descending order
print("numbers sorted descending order ", nums)

print("min of num", min(nums))  # min value
print("max of num", max(nums))  # max value
print("sum of num", sum(nums))  # sum value

# Exercise 4 = Tuples
# ------------------------------------------------------------------------
# Tuples are immutable compared to list - This is the only difference
# list
print("\nExercise 4")
list_1 = ["Jon", "Jacob", "Bob"]
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = "Samantha"
print(list_1)
print(list_2)

# Tuples
print("\nTuples")
tuple_1 = ("Jon", "Jacob", "Bob")
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# Exercise 5 = Set -  These are values that are unordered and have no duplicates
# ------------------------------------------------------------------------
print("\nExercise 5")

"""
Sets don't care about order 
sets are a good way to get rid of duplicates  
"""
cs_courses = {"Computer Security", "Networking", "OOP", "Data Structure", "Algorithm",
              "Algorithm"}  # notice it will not print Algorithm twice
print(cs_courses)
print("Algorithm" in cs_courses)

art_courses = {"painting", "drawing", "cad", "Algorithm", "Computer Security", "Networking", "OOP", }
print("intersection", cs_courses.intersection(art_courses))
print("Difference", cs_courses.difference(art_courses))  # checking the difference between the two sets
print("union", cs_courses.union(art_courses))  # creating a union between the

# How to create empty: List, Tuples and Sets

# Empty list
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuples = ()
empty_tuples = tuple()

# Empty Sets
empty_set = {}  # This isn't right! Its a dictionary
empty_tuples = set()
