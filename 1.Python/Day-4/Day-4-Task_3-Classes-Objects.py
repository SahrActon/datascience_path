# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer

# Task 1 - creating a class
print("\nTask 1 - creating a class")


class MyClass:
    x = 5


print(MyClass)

# Task 2 - Creating an object
print("\nTask 2 - Creating an object")
p1 = MyClass()
print(p1.x)

# Task 3 -
print("\nTask 3 - built-in __init__() function")
"""using the built-in __init__() function
All classes have a function called __init(), which is always executed when the class is being initiated
Use the __init__() function to assign values to object properties, or other operations that are necessary to do 
when the object is being created  
"""

""" 
It is important to note that the 
    __init__ function is called automatically every time the class is being used to create a new object
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 26)

print(p1.name)
print(p1.age)

# Task 4 - Object methods
print("\nTask 4 - Object methods")

"""
Objects can also contain methods. 
Methods in objects are function that belong to the object 
"""


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p2 = Person2("Thomas", 22)
p2.myfunc()

# Task 5 - THe self
"""
The self parameter is a reference to the current instance 
to the class and is used to access variables that belong to the class. 
It doe not have named self, you call is whatever you like, but it have the first parameter of any class
"""
print("\nTask 5 -")


class Person:
    def __init__(mysillyObject, name, age):
        mysillyObject.name = name
        mysillyObject.age = age

        def myfucntion(abc):
            print("hello my name is " + abc.name)

            # the code below will print out nothing because height does not exist
            print("hello my name is " + abc.height)


p3 = Person2("Bob", 67)
p3.myfunc()

# Task 6 - Modifying object Properties
print("\nTask 6 -")


class Person4:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def getName(self):
        print("Your name is " + self.name)


p1 = Person4("Thomas", 27, 180)
p1.getName()
p1.name = "Bobby Smith"

p1.getName()

# Task 7 - Deleting an object per
# you can delete a property of an object using the del keyword:
print("\nTask 7 -")


class Person4:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def getName(self):
        print("Your name is " + self.name)


p1 = Person4("Thomas", 27, 180)
p1.getName()
p1.name = "Bobby Smith"

del p1.name
# p1.getName() # this will product an error you if try to print it out


# Task 8 - the pass statement
print("\nTask 8 -")


# the class definitions cannot be empty, but if you do need it to be empty used the
# keyword pass

class Person:
    print("we have the word pass ")
    pass


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
