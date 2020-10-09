# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=6

# Rule - If you want to code well - No Copying and Pasting of code

# Boolean represents one of two values "True" or "False"
# You can evaluate any expression in Python, and get one of two answers, "True" or "False"
# When you compare two values, the expression is evaluated and python returns a boolean answer.

# Task 1
print('\nTask1')
print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

# Task 2

print('\nTask2')

a = 30
b = 40

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a ")

# Task 3
print('\nTask3')
# Evaluate values and variables
# Using the "bool()" function allows you to evaluate any value and give you "True or "False" in return

print(bool("Hello"))
print(bool(15))

# Task 4
print('\nTask4')
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Task 5
print('\nTask5')
# Most values are "True"
# Almost any value is evaluated to True , if it has some sort of content.
# Any String is "True" expect empty String.
# Any number is "True", except 0.
# Any list, tuple, set and dictionary are "True", except empty ones.

print(bool(""))  # empty String
print(bool("Hello Python"))  # String

print(bool(0))  # this should be false
print(bool(4))  # this should be "True"

print(bool([]))  # empty list
print(bool(["apple", "banana", "mango"]))  # list

# Task 6
print('\nTask 5')
# These values will always return false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))  # tuple
print(bool([]))  # list
print(bool({}))  # Set

# Task 7
print('\nTask 7')
'''
One more value, or object in this case, evaluates to "False", 
and is if you have an object that is made from a class with a __len__ function that return 0 or "False" 
'''


class myclass():
    def __len__(self):
        return 0


testingBool = myclass()
print(bool(testingBool))

# Task 8
print('\nTask 8')


# Function can return a boolen

def myFuction():
    return True


print(myFuction())

# Task 9
print('\nTask 9')


# simple condition checks Print "Yes" if the statement returns True, otherwise print "No!"

def myFunction():
    return True


if myFuction():
    print("Yes!")
else:
    print("No!")

# Task 10
print('\nTask 10')
x = 200
print(isinstance(x, int))
