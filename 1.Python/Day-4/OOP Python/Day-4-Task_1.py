# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer

# Classes and Instances

# Task 1 - Creating a class
# A class is a blue print for creating instances
print("\nTask 1 -")


class Employee:
    pass


emp1 = Employee()
emp2 = Employee()
print(emp1)
print(emp2)

# Instance variable
emp1.first = "Thomas"
emp1.lastName = "Acton"
emp1.email = "Thomas@company.com"
emp1.salary = 500000  #

# Instance variable
emp2.first = "bob"
emp2.lastName = "Acton"
emp2.email = "bob@company.com"
emp2.salary = 500000

print(emp1.first)

# Task 2 - Improved way of doing this
print("\nTask 2 -")


class Employee:
    def __init__(self, first_name, last_name, pay):  # this can be seen as a constructor
        self.firstName = first_name
        self.lastName = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.co.uk'


emp1 = Employee('Thomas', 'Acton', 500000)
emp2 = Employee('Bob', 'Acton', 500000)

print(emp1.email)
print(emp2.email)

# Task 3 - Adding methods
print("\nTask 3 -")


class Employee:
    def __init__(self, first_name, last_name, pay):  # this can be seen as a constructor
        self.firstName = first_name
        self.lastName = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.co.uk'

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)


emp1 = Employee('Thomas', 'Acton', 500000)
print(emp1.fullname())
emp2 = Employee('Bob', 'Acton', 500000)
print(emp2.fullname())

# Task 4 - Learning what happens if we were to leave out the self keyword
"""
This will pritn an error 
TypeError: fullname() takes 0 positional arguments but 1 was given
"""
print("\nTask 4 -")

# class Employee:
#     def __init__(self, first_name, last_name, pay):  # this can be seen as a constructor
#         self.firstName = first_name
#         self.lastName = last_name
#         self.pay = pay
#         self.email = first_name + '.' + last_name + '@company.co.uk'
#
#     def fullname():
#         return '{} {}'.format(firstName, lastName)
#
#
# emp1 = Employee('Thomas', 'Acton', 500000)
# print(emp1.fullname())
# emp2 = Employee('Bob', 'Acton', 500000)
# print(emp2.fullname())

# Task 5 -
print("\nTask 5 -")


class Employee:
    def __init__(self, first_name, last_name, pay):  # this can be seen as a constructor
        self.firstName = first_name
        self.lastName = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.co.uk'

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)


emp1 = Employee('Thomas', 'Acton', 500000)
emp2 = Employee('Bob', 'Acton', 500000)

emp1.fullname()  # <-- this code is whats getting transformed to the code below
Employee.fullname(emp1)  # emp1 passes the instance as self

print(emp1.fullname())
print(Employee.fullname(emp1))  # emp1 passes the instance as self
