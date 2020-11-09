# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer

"""
- The 'try' block lets you test a block of code for errors
- The 'expect' block lets you handle the error
- The 'finally' block lets you execute code, regardless of the result of the try - and expect blocks
"""

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message

# Task 1 - the try block will generate an error, because x is not defined
print("\nTask 1 - the try block will generate an error, because x is not defined")
try:
    print(x)
except:
    print("An exception occurred")

y = "hello"
try:
    print(y)
    print("pass")
except:
    print("An exception occurred")

# Task 2 - Many Exceptions
# You can define as many exception block as you want,
# e.g. if you want to execute a special block of code for special kind of error

print("\nTask 2 - The try block will generate a NameError, because x is not defined")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Task 3 - The try block does not raise any errors, so the else block is executed
print("\nTask 3 - The try block does not raise any errors, so the else block is executed")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Task 4 - Finally
print("\nTask 4 - Finally block, if specified, will be executed regardless if the try block raises an error or not")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Task 5 - The try block will raise an error when trying to write to ready-only file
print("\nTask 5 -")
try:
    file = open('demofile.txt')
    file.write("Hello new line")
except:
    print("Something went wrong when writing to the file")
finally:
    file.close()
# The program can continue, without leaving the file object open


# Task 6 - Raise an exception
# As a python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword
print("\nTask 6 - Raise an error and stop the program if x is lower 0")
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Task 7 - The raise keyword is used to raise an exception
# You can define what kind or error to raise, and the text to print to the user
print("\nTask 7 - Raise a Type Error if x not an integer")
x = "hello"
if not type(x) is int:
    raise TypeError("Only Integers are allowed")

# Task 8 -
print("\nTask 8 -")
