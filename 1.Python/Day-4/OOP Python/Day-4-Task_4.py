# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer

#  Python Inheritance

# Task 1 -
print("\nTask 1 - Creating an inheritance class for developer")


class Employee:
    # class variable
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

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # accessing them through the instance


class Developer(Employee):
    # setting the raise amount to 10% instead of the standard 4%
    raise_amount = 1.10


emp_1 = Employee("Employee_1", "Coder", 100000)
emp_2 = Employee("Employee_2", "Coder", 100000)

""" 
Method resolution order - This is really usefully
because it allows us to see the method resolution order 
"""
# print(help(Developer))

print(emp_1.email)
print(emp_2.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print("Creating developer instances using Employee class")
print('\n')
dev_1 = Developer("Top", "Coder", 100000)
dev_2 = Developer("God", "Coder", 100000)

print(dev_1.email)
print(dev_2.email)

# Task 2 - printing out the raise amount
print("\nTask 2 -")

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Task 3 - passing for parameters for developers
print("\nTask 3 - passing for parameters for developers")


class Developer(Employee):
    # setting the raise amount to 10% instead of the standard 4%
    raise_amount = 1.10

    # this can be seen as a constructor
    def __init__(self, first_name, last_name, pay, programming_language):
        super().__init__(first_name, last_name, pay)  # this will inherited from employee
        # Employee.__init__(first_name, last_name, pay)  # we can also write the code like this
        self.programming_language = programming_language


print("Creating developer instances using Employee class")
dev_1 = Developer("Top", "Coder", 100000, "Python")
dev_2 = Developer("God", "Coder", 100000, "Java")
print('\n')
print('\t', dev_1.email)
print('\t', dev_1.programming_language)

# Task 4 - Creating a manager class
print("\nTask 4 - Creating a manager class")


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # def add_emp(self, emp):
    #     if emp not in self.employees:



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
