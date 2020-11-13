# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer

# Task 1 - To make sure a string will display as expected, we can format the result with the format() method
# To control control such values, add placeholder (curly brackets {}) in the text,
# and run the values through format() method

print("\nTask 1 - Place holder")
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Task 2 -
print("\nTask 2 - Place holder")
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Task 3 - Multiple values
print("\nTask 3 -")
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Task 4 - Index Numbers
# You can use index numbers (a number side the curly brackets {0}) to be
# sure the values are placed in the correct placeholders
print("\nTask 4 -")
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Task 5 - also if you want to refer to same value more than once, use the index number
print("\nTask 5 -")
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Task 6 - Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use the names when you pass the parameter values
# txt.format(carname = "Ford")
print("\nTask 6 -")
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Bentley", model="Continental GT"))

# Task 7 -
print("\nTask 7 -")

# Task 8 -
print("\nTask 8 -")

# Task 9 -
print("\nTask 9 -")
