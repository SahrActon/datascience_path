# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer

# Class variables

# Task 1 - class variables
print("\nTask 1 -")


class Employee:
    # class variable
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):  # this can be seen as a constructor
        self.firstName = first_name
        self.lastName = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.co.uk'

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)  # accessing them through the instance


emp1 = Employee('Thomas', 'Acton', 500000)
emp2 = Employee('Bob', 'Acton', 600000)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# print(emp1.__dict__)
# print(emp2.__dict__)
#
# print(Employee.__dict__)

"""
 this will apply a global change
 this will allow it make a change on the class as well as all of the instances of the class
"""
Employee.raise_amount = 1.05

emp1.apply_raise()  # we have changed the value for raise globally
print("Previous value ", emp1.pay)  # this is use ing the new value of 1.05 instead of 1.04

Employee.raise_amount = 1.04  # setting it back to the original value

# now we only want to give a raise to one special person
emp1.pay = 500000  # setting back the original pay
emp1.raise_amount = 2.0  # doubling their pay  only this instance will have this value

print('\n')
print(emp1.__dict__)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp1.apply_raise()
print("New Raised value", emp1.pay)

# Task 2 - Places where is does't make sense to use self
print("\nTask 2 -")


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


print(Employee.num_of_emps)  # this should print out 0 because we have not created any employees yet
emp1 = Employee('Thomas', 'Acton', 500000)
emp2 = Employee('Bob', 'Acton', 600000)
print(Employee.num_of_emps)  # this should print out 2 because we have created 2 employees


# Task 3 -
print("\nTask 3 -")

# Task 4 -
print("\nTask 4 -")

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
