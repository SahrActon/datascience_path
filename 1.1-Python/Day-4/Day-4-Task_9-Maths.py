# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer

# Python has a set of built-in math functions, including an extensive math module, that allows you
# to perform mathematical task on numbers

# Task 1 - Built-in Math functions
# The min() and max functions can be used to find thw lowest and highest value in an iterable
print("Task 1 - Built-in Math functions")
x = min(5, 10, 15, 20)
y = max(5, 10, 15, 20)
print("The min value is", x)
print("The max value is", y)

# Task 2 - the abs() function returns the absolute(positive) value of the specified number:
print("\nTask 2 - the abs")
x = abs(-7.25)
print(x)

# Task 3 - The pow
print("\nTask 3 - The pow")
# The pow(x,y) function returns the value of x to the power of  y(x^y).
# return the value of 4 to the power of 3 (same as 4 * 4 * 4)
x = pow(4, 3)
print(x)

# Task 4 - The Math Module
# Python has a built-in nodule called math, which extends the list of mathematical functions
# To use it, you must import the math module
# When you have imported the math module, you can start using methods and constants of the module.
# The math.sqrt() method for example returns the square root of a number
print("\nTask 4 - The Math Module")
import math

x = math.sqrt(64)
print(x)  # this should print out 8
x = math.sqrt(16)
print(x)  # this should print out 4

print("\nTask 4.2 - The Math Module")

x = math.ceil(1.4)  # the ceil() method rounds a number upwards to its nearest integer and returns the result
y = math.floor(1.4)  # the floor() method rounds a number downwards to its nearest integer and returns the result

print(x)  # this will return 2
print(y)  # this will return 1

# Task 5 - maths.pi - constant, returns the value of PI(3.14)
print("\nTask 6 -  math.pi")
import math

x = math.pi
print(x)
