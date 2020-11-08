# source - > https://www.w3schools.com/python/python_datetime.asp


# Task 1 - Python
import datetime

print("Task 1 - Python Dates")
x = datetime.datetime.now()
print(x)

# The date contains year, month, day, hour, minute, second and microsecond
# The datetime module has many methods to return information about the date object
# Task 2 -
print("\nTask 2 - Date output")
print(x.year)
print(x.strftime("%A"))  # %A	Weekday, full version

# Task 3 - Creating Dae Objects
print("Task 3 - Creating Dae Objects")

# The datetime() class also takes parameters for time and timezone
# hour, minute, second, microsecond, tzone, but they are optional, and has a default value of ,
# none for timezone
x = datetime.datetime(2020, 11, 5)
print(x)

# Task 4 - The strtime() method
# The datetime object has a method for formatting date object into readable strings
# the method called strtime(), and takes one parameter, format, to specify the format of the returned string
print("Task 4 -")

print(x.strftime("%B"))  # %B	Month name, full version
# Task 5 -
print("Task 5 -")

# Task 6 -
print("Task 6 -")

# Task 7 -
print("Task 7 -")

# Task 8 -
print("Task 8 -")
