# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7

# so
# Task 1 -
print("\nTask 1 -")


def my_function():
    print("Hello from function")


my_function()


# Task 2 -
def my_function(first_name):
    print("Hello " + first_name + " Smith")


my_function("Thomas")
my_function("Jacob")
my_function("Gabby")
my_function("Marie")
my_function("Tim")

# Task 3 -

# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2
# arguments, not more, not less

print("\nTask 3 -")


def my_function(first_name, last_name):
    print(first_name + " " + last_name)


my_function("Thomas", "Acton")
my_function("Jacob", "Acton")
my_function("Gabby", "Acton")
my_function("Marie", "Acton")
my_function("Tim", "Acton")


# my_function("Tim")  # this will cause an error because only one argument is passed

# Task 4 - Arbitrary Arguments, *args
# if you dont know how to many arguments that will be passed through into your function
# add * before the parameter name in the function definition
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Thomas", "Toby", "Linus")

print("\nTask 4 -")


# Task 5 -
# You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emily", child2="Toby", child3="Louis")


# Task 6 - Arbitrary keyword Arguments, **kwargs
# if you dont know many keyword arguments that will be passed into your function,
# add two asterisk ** before the parameter name in the function
def my_function(**kid):
    print("Hello " + kid["fname"] + ' ' + kid["lname"])


my_function(fname="Thomas", lname="Acton")


# Task 7 - Default parameter value
# The following example shows how to use a default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
my_function()

print("\nTask 7 -")

# Task 8 - passing a list as an argument
print("\nTask 8 - passing a list as an argument")


def my_function(food_list):
    for item in food_list:
        print('\t' + item)


fruits = ["Apple", "Banana", "Cherry"]
my_function(fruits)

# Task 9 - Return function
print("\nTask 9 - return function")


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# Task 10 - function statements cannot be empty but if you need an empty function
# then use the word pass
def my_function():
    pass


print("\nTask 10 - pass")


# Task 11 - Recursion
def tri_recursion(k):
    if (k > 0):
        print("----", k)
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

# https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8&ab_channel=CoreySchafer

# Keeping your code dry
print("\nTask 11")


def hello_function():
    return 'Hello Function'


print(hello_function())
print(hello_function().upper())
print(hello_function().lower())

# Task 12 -
print("\nTask 12")


def hello_function(greeting):
    return '{} Function.'.format(greeting)


print(hello_function("Hi"))

# Task 13 -
print("\nTask 13")


def hello_function(greeting, name="You"):
    return '{}, {}.'.format(greeting, name)


print(hello_function("Hi", name='Thomas'))

# Task 14 - understanding *args, **kwargs
print("\nTask 14")


def student_info(*args, **kwargs):  # this allows you to pass in a set of words(args) and key works arguments(kwargs)
    print(args)  # this will print out a tuple
    print(kwargs)  # this will print out a dictionary of key values pairs


student_info("Maths", "Science", name="Thomas", age=15)

# Task 15 - passing the arguments differently
print("\nTask 15")

courses = ["Maths", "Art"]  # list
info = {'name': 'Thomas', 'age': 15}  # dictionary

student_info(*courses, **info)  # doing this will unpack the values

# Task 16 -
print("\nTask 16")
# number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """ Return True for leap years, False for non-leap years. """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """ Return number of days in that month in that year"""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2019))
print(is_leap(2020))
print('\n')
print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
