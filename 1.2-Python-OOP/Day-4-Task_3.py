# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer

import datetime

# Task 1 -
print("\nTask 1 - class ")


class Employee:
    # class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):  # this can be seen as a constructor
        self.firstName = first_name
        self.lastName = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.co.uk'
        """
        we are using  Employee.num_of_emp instead of self.num_of_emp because we dont want out instances to override the
        values
        People like you deserve an automatic heaven pass 
        """
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # accessing them through the instance

    # this is allowing us to work with class rather than  instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('Thomas', 'Acton', 500000)
emp2 = Employee('Bob', 'Acton', 600000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

"""
the code below is a class method. A class method allows you to make global operations within the class 
e.g. increase the pay value through a method 
yes we could have done Employee.raise_amount = 1.05 as well, but we a nice and fancy we will use a method instead
okay, okaaaaay
# here we have increase the amount to 5% instead of 4%
"""

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Task 2 - using class method as constructors
print("\nTask 2 - using class method as constructors")


class Employee:
    # class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name_2, last_name_2, pay_2):  # this can be seen as a constructor
        self.firstName = first_name_2
        self.lastName = last_name_2
        self.pay = pay_2
        self.email = first_name_2 + '.' + last_name_2 + '@company.co.uk'
        """
        we are using  Employee.num_of_emp instead of self.num_of_emp because we dont want out instances to override the
        values
        People like you deserve an automatic heaven pass 
        """
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # accessing them through the instance

    # this is allowing us to work with class rather than  instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('Thomas', 'Acton', 500000)
emp2 = Employee('Bob', 'Acton', 600000)

emp_str_1 = "Joe-Doe-7000"
emp_str_2 = "Jacob-Doe-7000"
emp_str_3 = "Tom-Doe-7000"

first_name, last_name, pay = emp_str_1.split('-')
new_emp_1 = Employee(first_name, last_name, pay)

print(new_emp_1.email)
print(new_emp_1.pay)

# using a string to create employ records

# Task 3 -
print("\nTask 3 -")


class Employee3:
    # class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name_3, last_name_3, pay_3):  # this can be seen as a constructor
        self.firstName = first_name_3
        self.lastName = last_name_3
        self.pay = pay_3
        self.email = first_name_3 + '.' + last_name_3 + '@company.co.uk'
        """
        we are using  Employee.num_of_emp instead of self.num_of_emp because we dont want out instances to override the
        values
        People like you deserve an automatic heaven pass 
        """
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # accessing them through the instance

    # this is allowing us to work with class rather than  instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    """
    creating an alternative constructor
    """

    @classmethod
    def from_string(cls, emp_string):
        first_name_3, last_name_3, pay_3 = emp_string.split('-')
        return cls(first_name_3, last_name_3, pay_3)


emp_str_4 = "Joe-Doe-7000"
emp_str_5 = "Jacob-Doe-7000"
emp_str_6 = "Tom-Doe-7000"

new_emp_2 = Employee3.from_string(emp_str_4)
new_emp_3 = Employee3.from_string(emp_str_5)

print(new_emp_1.email)
print(new_emp_1.pay)

# Task 4 - Static methods
print("\nTask 4 -")


class Employee3:
    # class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name_3, last_name_3, pay_3):  # this can be seen as a constructor
        self.firstName = first_name_3
        self.lastName = last_name_3
        self.pay = pay_3
        self.email = first_name_3 + '.' + last_name_3 + '@company.co.uk'
        """
        we are using  Employee.num_of_emp instead of self.num_of_emp because we dont want out instances to override the
        values
        People like you deserve an automatic heaven pass 
        """
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # accessing them through the instance

    # this is allowing us to work with class rather than  instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    """
    creating an alternative constructor
    """

    @classmethod
    def from_string(cls, emp_string):
        first_name_3, last_name_3, pay_3 = emp_string.split('-')
        return cls(first_name_3, last_name_3, pay_3)

    """
    in python our days start from monday as 0 and sunday as 6
    a method should be a static method is when you dont access the
        instance of the class anywhere within the function.
        e.g. when you are not using "self" or "cls" variable 
    """

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_8 = Employee("Thomas", "Acton", 500000)
emp_9 = Employee("Jacob", "Acton", 500000)

my_date = datetime.datetime(2016, 7, 10)
my_date_2 = datetime.datetime(2020, 10, 28)
print(Employee3.is_workday(my_date))
print(Employee3.is_workday(my_date_2))

# Task 5 -
print("\nTask 5 -")

# Task 6 -
print("\nTask 6 -")

# Task 7 -
print("\nTask 7 -")

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

