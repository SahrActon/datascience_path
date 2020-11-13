#

# A dictionary is a collection which is ordered, changeable and indexed.
# In python dictionary are written with curly brackets and they have keys and values
# source used https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5&ab_channel=CoreySchafer


# Task 1 -
print("Task 1")
student = {"name": "John", "age": 23, "courses": ['Math', 'English']}
print(student['name'])
print(student['age'])
print(student['courses'])
# print(student['phone']) # this will give a key error
print(student.get('courses'))
print(student.get('phone'))  # this will print out none because it does not exist
print(student.get('phone', ' Not found'))  # if its not we will print out "not found" for example

# Task 2 - adding a new entry
student['phone'] = '11111-22222'
print("Task 2")
print(student.get('phone'))  # this will print out none because it does not exist

# Task 3 - updating values
print("Task 3")
student['name'] = "Thomas"
print(student)
student.update(
    {'name': "Frank ", "age": 27,
     "height": "6ft"})  # we can also use the update method to update your value for a given key
print(student)

# Task 4 - remove
print("Task 4")
del student['age']
student.update(
    {'name': "Frank ", "age": 27,
     "height": "6ft"})  # we can also use the update method to update your value for a given key

height = student.pop("name")
print(student)

# Task 5 - check the length - this will shows the numbers of keys that we have
print("Task 5")
student.update(
    {'name': "Frank ", "age": 27,
     "height": "6ft"})  # we can also use the update method to update your value for a given key
print(len(student))

# Task 6 - printing all our keys
print("Task 6")
print(student.keys())

# Task 7 - printing all our values
print("Task 7")
print(student.values())

# Task 8 - printing all keys and values
print("Task 8")
print(student.items())

# https://www.w3schools.com/python/python_dictionaries.asp
# Task 9 - Looping through the keys and values
print("Task 9")

for key, value in student.items():
    print('\t', key, ':', value)

# Task 10 -
print("Task 10")
thisdict = {
    "brand": "Bentley",
    "model": "Continental",
    "year": 1994
}
print('\t', thisdict)

# Task 11 -
print("Task 11")
x = thisdict["model"]
print('\t', x)

# Task 12 - get method
print("Task 12")
x = thisdict.get("model")
print('\t', x)

# Task 13 - changing the values
print("Task 13")
thisdict["model"] = "Continental convertible"
print('\t', thisdict)

# Task 14 - Loop through the dictionary
print("Task 14")
for x in thisdict:
    print('\t', x)  # this will print out the keys

# Task 15 - # this will print out the values
print("Task 15")
for x in thisdict:
    print('\t', thisdict[x])

# Task 16 - we can also print print the values using the values() method
print("Task 16")
for x in thisdict.values():
    print('\t', x)  # this will print out the values

# Task 17 - print out the key and values
print("Task 17")
for key, value in thisdict.items():
    print("\t", key, value)

# Task 18 - checking if key exists
print("Task 18")
if "model" in thisdict:
    print("\t", "Yes we have model in the dictionary")

# Task 20 - checking to see the number of keys we have
print("Task 20")
print('\tWe have', len(thisdict), "keys")

# Task 21 - adding items
print("Task 21")
thisdict["color"] = "space grey"
print('\t', thisdict)

thisdict.update({"gears": 6})
print('\t', thisdict)

# Task 22 - Remove
print("Task 22")
gears = thisdict.pop("gears")
print('\t', thisdict)

# Task 24 - pop() the last item
print("Task 24")
thisdict.popitem()
print('\t', thisdict)

# Task 25 - using the delete
print("Task 25")
thisdict = {
    "brand": "Bentley",
    "model": "Continental",
    "year": 1994,
    "color": "space grey"
}
del thisdict["model"]
print('\t', thisdict)

# Task 26 -
'''
You can not copy aa dictionary simply by typing "dict2" - "dict1", because dict3 will not be a reference to dict1,
and changes made in "dict1" will be automatically also be made in "dict2"
    There are ways to make a copy, one way is to copy, using the copy() method 
'''
print("Task 26")
thisdict = {
    "brand": "Bentley",
    "model": "Continental",
    "year": 1994,
    "color": "space grey"
}
thisdict2 = thisdict.copy()
print('\t', thisdict2)
# another way of copying is to use the built-in function dict()
thisdict3 = dict(thisdict)
print('\n\t', thisdict3)

# Task 27 -
print("Task 27")

myfamily = {
    "child1": {
        "name": "Tom",
        "age": 27
    },
    "child2": {
        "name": "Jacob",
        "age": 23
    },
    "child3": {
        "name": "Alex",
        "age": 30
    },
    "child4": {
        "name": "bill",
        "age": 55
    },
}
print('\t', myfamily)

child1 = {
    "name": "Tom",
    "age": 27
}

child2 = {
    "name": "Jacob",
    "age": 23
}
child3 = {
    "name": "Alex",
    "age": 30
}
child4 = {
    "name": "bill",
    "age": 55
}

myfamily2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
    "child4": child4
}
print('\t', myfamily2)

# Task 28 - creating a dictionary the long way
print("Task 28")

# Task 29 - construct a dictionary using the key word
print("Task 29")
thisdict = dict(brand="Ford", model="Mustang", year=1994)
print("\t", thisdict)

# Task 30 -
print("Task 30")
