import mymodule as mx

mx.greeting("Thomas")

a = mx.person["age"]
print(a)

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a module
# you can create an alias when you import a module, by using the "as" keyboard

# Built-in Modules
# These are several built-in modules in python, which you can import whenever you like


print("\nTask 2")
# import and use the platform module
import platform

x = platform.system()
print(x)

# Using the dir() function names (or variable names) in a module. The dir() function
# The dir() function can be used on all modules, also the ones you create yourself
print("\nTask 3")
x = dir(platform)
print(x)

# tyring dir on my own python file
print("\nMy own python file")
print(dir(mx))

# import from Module
# You can choose to import only parts of your module, by using the "from" keyword.

# Example
# The module named mymodule has one function and one dictionary
from mymodule import person

print("\n")
print(person["age"])
