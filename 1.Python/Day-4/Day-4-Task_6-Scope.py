# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer

"""
A variable is only available from inside the region it is created.
    This is called scope
"""

# Task 1 - Python Scope
# A variable created inside a function is available inside the function
print("\nTask 1 - Python Scope")


def myfunc():
    x = 200
    print(x)


myfunc()

# Task 2 - function inside a function
# As explained in the example above, the variable "x" is not available outside the function,
# but it available for any function inside the function
print("\nTask 2 - function inside function ")


def myfunction():
    x = 400

    def myinnerfunction():
        print(x)

    myinnerfunction()


myfunction()

# Task 3 - Global scope
# A variable created in the main body of the python code is a global variable
# and belongs to the global scope

print("\nTask 3 - Global scope")
x = 300


def myFunction():
    print(x)


myFunction()
print(x)

# Task 4 - Name variables
# if you operate with the same variable name inside and outside of a function,
# Python will treat them as two separate variable, one available in the global scope (outside the function)
# and one available in the local scope (inside function):

# The function will print the local "x" and then the code will print global x
print("\nTask 4 -")
x = 4


def myFunction():
    x = 200
    print(x)


myFunction()
print(x)

# Task 5 - Global keyboard
# if you need to create a global variable, but are stuck in the local scope, you can use the global keyboard
# the "global" keyword makes the variable global

# if we use the global keyword, the variable belongs to the global scope
print("\nTask 5 - the Global keyword")


def myfunc():
    global x
    x = 77


myfunc()
print(x)

print("\nTask 5.2 - the Global keyword")
# Also, use the global keyword if you want to make a change to a global variable inside a function
# To change the value of a global variable inside a function, refer to the variable by using the global keyword

x = 1.5


def myFunc():
    global x
    x = 200


myFunc()
print(x)

# Task 7 -
print("\nTask 7 -")

# Task 8 -
print("\nTask 8 -")
