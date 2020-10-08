# Working with string
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2&ab_channel=CoreySchafer

my_message = 'Hello world'
print(my_message)

my_message = 'Hello\'s world'  # This allows you escape the word hello's
print(my_message)

my_message = """Hello, this is a really long message 
and i am still writing 
wow 
we are still 
going
!
"""
print(my_message)

my_message = "Hello World"
print((my_message[10]))
print((my_message[0:5]))
print((my_message[:5]))

# String methods
print(my_message.lower())  # Convert the whole word into lower case
print(my_message.upper())  # Convert the whole word into upper case
print(my_message.count("Hello"))  # Count how many times the given string occurs in our string variable
print(my_message.count("l"))  # Count how many times the given string occurs in our string variable
print(my_message.find("Hello"))  # Find where the string starts from within our variable
print(my_message.find("World"))  # Find where the string starts from within our variable

# Replacing string
new_message = my_message.replace("World", "Thomas")
print(new_message)

# Adding multiple strings
greeting = "Greetings"
name = "Thomas"

message = greeting + ', ' + name + '. ' + "Welcome!"
print(message)

# Working with place holders
message = '{}, {}. Welcome!'.format(greeting, name, )
print(message)

# Working with f string
message = f'{greeting.upper()}, {name.lower()}. Welcome!'
print(message)

# Working dir functions
# print(dir(name))
# print(help(str))  # this will help your see the list of functions/ information about a function / primitive type

# Source - https://www.w3schools.com/python/python_strings.asp

"""
String literals in python are surrounded by either single quotation marks, or double quotation marks 
"""
print('\nPart 2')
print("Hello")
print('Hello')

a = "hello"
print(a)

# Multiline Strings
a = """
Hello,
Multiline 
String
!
"""
print(a)

a = '''
Hello,
Multiline
String
!
'''
print(a)

a = "Hello World"
print(a[1])

b = "Hello, World"
print(b[2:5])

# Negative Indexing
# get the characters from position 5 to position 1(not included, starting from the count from the end of the string
b = "abcd, efghij"
print(b[-5:-2])

# String length
a = "Hello, Tom"
print(len(a))

# removing white spaces
a = " Hello, World! "
print(a.strip())  # removes the spaces from the start and the end of the string

# returns the string to Lower case
a = " Hello, World! "
print(a.lower())

# returns the string to upper case
a = " Hello, World! "
print(a.upper())

# replace method

a = " Hello, World! "
print(a.replace("H", "J"))  # bad way

a = " Hello, World! "
b = a.replace("H", "J")
print(b)  # good way

# Splitting the string

a = "Hello, World!"
print(a.split(","))  # uses the character that you have specified to split with

# Checking if string is in or not
my_text = "The rain in Spain stays mainly in the plain"
x = "ain" in my_text
print(x)

x = "ain" not in my_text
print(x)

# string concatenation
a = "Hello"
b = "World"
c = a + ' ' + b
print(c)

# String formatting
quantity = 3
itemno = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} pounds"
print(my_order.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
my_order = "I want to pay {2} pounds for {0} pieces of item {1} "
print(my_order.format(quantity, itemno, price))

# better way of string formatting

quantity = 3
itemno = 567
price = 49.95
# message = f'{greeting.upper()}, {name.lower()}. Welcome!'
my_order = "I want to pay " + f'{quantity}' + " pounds for " + f'{itemno}' + " pieces of item " + f'{price}'
print(my_order)

# Escape Character
# To insert characters that are illegal in a string, use an escape character
# we can use a backslash \ followed by the character tou to insert

# Illegal example
# txt = "We are the so-called" Kings " from africa."
txt = "We are the so-called \"Kings\" from africa."
print(txt)

# \' Single Quote
txt = 'It\'s alright'
print(txt)
more_txt = 'Hello i\'m a man that\'s humble and outgoing'
print(more_txt)

# \\	Backslash
txt_back_slash = "This is will insert \\ (one backslash)"
print(txt_back_slash)

txt_back_slash = "This is will insert \\\\ (two backslash)"
print(txt_back_slash)

# \n	New Line
hello = 'Hello\nNewLine\nline1\nline2'
print(hello)
# \r	Carriage Return
print('\n')
hello = "Acton\rChipmunk is the best driller grime mc! Facts!"
print(hello)

# \t	Tab
txt = "Hello\tWorld!"
print(txt)

# \b	Backspace
# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

# \f	Form Feed
#
#
