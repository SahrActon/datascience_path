# source -> https://www.w3schools.com/python/python_json.asp


# Task 1 - Python Json
# JSON is a syntax for storing and exchange data
# JSON is text written with javascript object notation
# Python has a built-in package called "json" which can be used to work with JSON data.
import json

print("Task 1 - Parsing json - covert from JSON to python")
# if you have a json string string, you can parse it by using the json.loads() method

# creating a JSON object
x = '{"name":"Thomas" , "age":30, "country":"United Kingdom"}'

# parse
y = json.loads(x)

# the result is a Python dictionary
print(y["age"])

# Task 2 - Convert from Python to JSON
# if you have a Python object, you can convert it into a json by using the json.dumps() method
print("Task 2 - Convert from python to JSON")

x = {
    "name": "Bobby",
    "age": 20,
    "country": "Hogwarts"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSONs string
print(y)

# Task 3 - Converting python objects
# we can convert the following types, into JSON strings
"""

- dict
- list
- tuple
- string
- int 
- float 
- True
- False
- None

"""
print("\nTask 3 - Converting python objects")
print(json.dumps({"name": "Marie", "age": 44}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Task 4 - Convert a python object containing all the legal data types
print("\nTask 4 - Convert a python object containing all the legal data types")
x = {
    "name": "Jonathan",
    "age": 35,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": ["Bruce", "Fella"],
    "cars": [
        {"model": "Bentley Continental", "numOfSeats": 4},
        {"model": "Ford Focus", "numOfSeats": 4}
    ]
}

print(json.dumps(x))

# Formatting the result
# Use the indent parameter to define the numbers of indents
print('\n', json.dumps(x, indent=1))

# You can also define the separators, default value is (",", ":"), which means using a comm
# and a space to separate each object, and a colon and a space to separate keys from values
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, separators=(". ", " * ")))
print(json.dumps(x, indent=4, sort_keys=True))

# Task 5 -
print("Task 5 -")

# Task 6 -
print("Task 6 -")

# Task 7 -
print("Task 7 -")

# Task 8 -
print("Task 8 -")

# Task 9 -
print("Task 9 -")

# Task 10 -
print("Task 10")
