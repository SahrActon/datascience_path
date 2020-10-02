# Variables are containers for storing data values

# Exercise 1
print("Exercise 1")
x = 5
y = "John"
print(x)
print(y)

# Exercise 2
print("\nExercise 2")
x = 4  # x is of type int
x = "Sally"  # x is now type str
print(x)

# Exercise 3 - Strings can be declared either with single or double quotes
print("\nExercise 3")
x = "John"
# is the same as
x = 'John'
print(x)

# Exercise 4
print("\nExercise 4")
"""
variables rules 
-------------------
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# Legal names
myvar = "John"
my_var = "John"  # 1st preference
_my_var = "John"  # 2nd preference
myVar = "John"
MYVAR = "Joh "  # this looks horrible to me :/
myvar2 = "John"

"""
# Illegal variables names
2myvar  = "John"
my-car = "John"
my car = "John"
"""

# Exercise 5
# Python allows you to assign multiple variables on one line
print("\nExercise 5")
x, y, z = "One", "Two", "Three"
print(x)
print(y)
print(z)
print(x, y, z)

# Exercise 6

print("\nExercise 6")
x = y = z = "Orange"
print(x)
print(y)
print(z)
print(x, y, z)

# Exercise 7 - Output variables
"""
The python print statement is often used to output variables 
To combine both text and a variable, Python uses the '+' character:
"""
print("\nExercise 7")
x = "awesome"
print("Python is " + x)

# Exercise 8
print("\nExercise 8")
x = "Python is "
y = "awesome"
z = x + y
print(z)

# Exercise 9
print("\nExercise 9")
x = 5
y = 10
print(x + y)

# Exercise 10
print("\nExercise 10")
# If you try to combine a string and a number, Python will output an error
x = 5
y = "John"
# print(x + y) # this outputs an error TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Exercise 11
print("\nExercise 11")
# Variables that are created outside a function (as in all of the examples above) are known aas global variables
# Global variables can be used by everyone, both inside of functions and outside
x = "Great"


def my_fun():
    print("Python is " + x)


my_fun()

# Exercise 12 - This is cool
print("\nExercise 12")
"""
When we create a variable with the same name inside a function, this variable will be local and can only be used inside the function. 
The global variables with the same name will remain as it was, global and with the original value
"""
x = "Awesome"


def my_func():
    x = "Fantastic"
    print("Python is " + x)


my_func()
print("Python is " + x)

# Exercise 13
print("\nExercise 13")


# Normally, when you create a variable inside a function,
#   that variable is local and can only be used inside that function
# To create a global variable inside a function, you use the "global" keyword

def my_function():
    global word
    word = "Fantastic and sweet"


my_function()

print("Python is " + word)

# Exercise 14
print("\nExercise 14")
"""
Also, use the "global" :keyword if you want to change a global variable inside a function 
"""
name = "Thomas"


def my_function():
    global name
    name = "Thomas Acton"


my_function()

print("My name is " + name)
