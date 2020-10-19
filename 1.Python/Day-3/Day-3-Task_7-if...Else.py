# https://www.w3schools.com/python/python_conditions.asp

# Task 1 -
print("Task 1 -")
a = 33
b = 200
if b > a:
    print("\t b is greater than a")

# Task 2 -
'''
The elif keyword states if the previous conditions were not true, 
    then try this condition    
'''
print("Task 2 -")
a = 33
b = 33
if b > a:
    print("\t b is greater than a")
elif a == b:
    print("\t a and b is equal")

# Task 3 -
'''
else keyboard catches anything which is not caught by preceding conditions
'''
print("Task 3 -")

a = 200
b = 33
if b > a:
    print("\t b is greater than a")
elif a == b:
    print("\t a and b is equal")
else:
    print("\t a is greater than b")

# Task 4 - pass
print("Task 4 -")
'''
"if" statements cannot be empty, if you have an if statements that doesnt
have any content then put in the pass statement to avoid getting an error 
'''
a = 33
b = 200

if b > a:
    pass

# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=6&ab_channel=CoreySchafer

# Task 5 -
print("Task 5 -if statements")
if True:
    print('\tConditional was True')

# Comparisons
# Equality: ==
# Not Equal: !=
# Greater than: >
# Less thank <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identity: is ( we have checking if the values are the same in memory

language = "Java"

if language == "Java":
    print('\tLanguage is Java')
elif language == "Python ":
    print('\tLanguage is Python')
elif language == "Java Script ":
    print('\tLanguage is Python')
else:
    print("\tNo Match found")

print("Task 6 -  boolean operation")
# Task 6 - boolean operation
# and
# or
# not
user = 'Admin'
logged_in = True

if user == "Admin" and logged_in:
    print("\tAdmin page")
else:
    print("\tBad Credentials")

# Setting logged_in to false
logged_in = False
if user == "Admin" and logged_in:
    print("\tAdmin page")
else:
    print("\tBad Credentials")

# Or
logged_in = True
if user == "Admin" or logged_in:
    print("\tAdmin page")
else:
    print("\tBad Credentials")

# Not
logged_in = True
if not logged_in:
    print("\t Please log in")
else:
    print("\tWelcome to our platform")

# Task 7 - Testing if objects are the same
print("Task 7 - ")
a = [1, 2, 3]
b = [1, 2, 3]

print("\t", a == b)  # The two objects have the same values
print("\t", a is b)  # These two objects do not point to the same address in memory

# Task 8 - using the built in id function
print('\t a Memory id is: ', id(a))
print('\t b Memory id is: ', id(b))

# Setting the id to to be the same
a = [1, 2, 3]
b = a
print("\t", a is b)  # These two objects do not point to the same address in memory

# Task 8 - using the built in id function
print('\t a Memory id is: ', id(a))
print('\t b Memory id is: ', id(b))

print("Task 8 -")
# False
# None
# Zero or any numeric types
# Any empty sequence: For example strings '', tuples(), list[]
# Any empty mapping: For example sets {}, dictionary {key:value}

# --------------------------------------------
condition = False

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
condition = None

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
condition = 0

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
condition = 10

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
condition = ''

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
condition = {}

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
condition = 'Test'

if condition:
    print("\tEvaluated to True")
else:
    print("\tEvaluated to False")
# --------------------------------------------
# Task 9 -
print("Task 9 -")

# Task 10 -
print("Task 10")

# Task 11 -
print("Task 11")

# Task 12 -
print("Task 12")

# Task 13 -
print("Task 13")

# Task 14 -
print("Task 14")

# Task 15 -
print("Task 15")

# Task 16 -
print("Task 16")

# Task 17 -
print("Task 17")

# Task 18 -
print("Task 18")

# Task 19 -
print("Task 20")
