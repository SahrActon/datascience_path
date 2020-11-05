# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer


# Task 1 -
print("\nTask 1 -")

# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the vaules
# Technically, in python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()
# Iterator vs iterable
# List, tuples, dictonaries and sets are all iterable objects. They are iterable containers which you can get from an iterator from.
# All these objects have a iter() method which is used to get an iterator

print(" 1.working with iterators")
my_tuple = ("apple", "banana", "orange")
my_iterator = iter(my_tuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print("\n 2.even strings are iterable objects and can return an iterator")
# even strings are iterable objects and can return an iterator:
my_string = "Hello Thomas"
my_iterator = iter(my_string)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Looping through an iterator
print("\n 3.Looping through an iterator")
my_tuple = ("apple", "banana", "orange")
for x in my_tuple:
    print(x)

# Looping through a string#
print("\n 3.Looping through a string")
my_string = "banana"

for x in my_string:
    print(x)

# Creating an iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to you object

class Mynumbers:
    def __iter__(self):
        self.a = 1
        # this is cool that you can return self.
        return self
