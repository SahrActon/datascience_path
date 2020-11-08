# https://www.w3schools.com/python/python_inheritance.asp
import datetime

# Task 1 - Python Inheritance
# Python inheritance allows us to define a class that inherits all the methods
# and properties from other class
# **** Parent class ****  - is the class being inherited, also classed a bass class
# **** Child class ****  - is the class#
# Create a Parent Class - Any class can be a parent class,
# so the syntax is the same as creating a class
print("\nTask 1 - Python Inheritance")


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(self.firstname, self.lastname)


# use the Person class to create an object, and then execute the printname method:

person_1 = Person("Thomas", "Acton")
person_1.print_name()

# Task 2 - Create a child Class
# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:

print("\nTask 2 -  Create a child Class")


class Student(Person):
    # use the pass keyword when you don want to add any other properties
    # or methods to the class
    pass


# Creating a student object and then execute the print name method
student_1 = Student("Mike", "Tyson")
student_1.print_name()

# Task 3 - Creating a student class
print("\nTask 3 - Creating a student class with  Person.__init__")


class Student(Person):
    # when we add the __init__ function,
    # the child class will no longer inherit the parents __init
    def __int__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)


student_1 = Student("Gabby", "Tyson")
student_1.print_name()

# Task 4 -
print("\nTask 4 - Creating a student class super()")


class Student(Person):
    # when we add the __init__ function,
    # using the super function will automatically inherit method and properties from its parents
    def __int__(self, firstname, lastname):
        super().__init__(firstname, lastname)


student_1 = Student("Micheal", "Tyson")
student_1.print_name()

# Task 5 - Adding Properties
print("\nTask 5 - Adding Properties to the child class")


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = datetime.datetime.now().year + 2


student_2 = Student("Bobby", "Tyson")
print(student_2.graduationyear)

# Task 6 - Add methods
print("\nTask 6 - Add methods")


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome " + self.firstname, self.lastname, "to the class of", self.graduationyear)


student_2 = Student("Babatunda", "Tyson", 2021)
student_2.welcome()

# Task 7 -
print("\nTask 7 - add methods")

# Task 8 -
print("\nTask 8 -")

# Task 9 -
print("\nTask 9 -")

# Task 10 -
print("\nTask 10")

# Task 11 -
print("\nTask 11")

# Task 12 -
print("\nTask 12")

# Task 13 -
print("\nTask 13")

# Task 14 -
print("\nTask 14")

# Task 15 -
print("\nTask 15")

# Task 16 -
print("\nTask 16")

# Task 17 -
print("\nTask 17")

# Task 18 -
print("\nTask 18")

# Task 19 -
print("\nTask 19")

# Task 20 -
print("\nTask 20")
