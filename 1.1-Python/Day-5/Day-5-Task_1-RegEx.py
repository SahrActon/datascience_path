# https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer

# A RegEx or Regular Expression, is a sequence of characters that forms a search pattern
# Regex can be used to check if a string contains the specified search pattern

# Task 1 - Search the string to see if it starts with "The" and ends with "Spain":
# this is the library for regex
import re

print('Task 1 - Search the string to see if it starts with "The" and ends with "Spain": ')
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a match!")
else:
    print("No match found")

# Task 2 - Metacharacters
# '[]' - Find a Set of characters - Example "[a-m]
print("\nTask 2 -")
# find all lower case character alphabetically between "a" and "m"
x = re.findall("[a-m]", txt)
print(x)

# find all upper case character alphabetically between "A" and "T"
x = re.findall("[A-T]", txt)
print("\n", x)

# '\' - Signals a special sequence (can also be used to escape characters - Example "\"
txt = "That will be 99 dollars"
# Find all digital characters
x = re.findall("\d", txt)
print("\n", x)

txt = "00000 00000000 ab"
# Find all digital characters
x = re.findall("\s", txt)
print("\n", x)

# '.' - Any character (expect new character) - Example "he..o"
txt = 'hello world'
# search for a sequence that starts with "he", followed by two (any) characters,
# and an "o":
x = re.findall("he..o", txt)
print("\n", x)

# "^" - start with - Example "^hello"
txt = 'hello world'
# check if the string starts with 'hello'
x = re.findall("^hello", txt)
if x:
    print("\nYes, the string starts with hello ")
else:
    print("\nNo Match")

# "$" - Ends with - Example "world$"
txt = 'hello world'
# check if the string starts with 'hello'
x = re.findall("world$", txt)
if x:
    print("\nYes, the string ends with world ")
else:
    print("\nNo Match")

"""
Matching 0, 1, or More Occurrences

* and +

* matches zero or more occurrences of the preceding character. The fewest possible occurrences of a pattern will satisfy the match.

Example: a*b will match b, ab, aab, aaab, aaaab, and so on.

+ matches one or more occurrences of the preceding character.

Example: a+b will match ab, aab, aaab, aaaab, and so on, but not just b.
"""
# "*" - Zero or more occurrences - Example "aix "
txt = "The rain in Spain falls mainly in the plain!"
# check if the string contains "ai" followed by 0 or more x characters
x = re.findall("aix*", txt)
print('\n', x)
if x:
    print("\nYes, there is at least one match ")
else:
    print("\nNo Match")

# "+" - One ore more occurrences - Example "ax+"
txt = "The rain in Spain falls mainly in the plain!"
# check if the string contains "ai" followed by 0 or more x characters
x = re.findall("aix+", txt)
print('\n', x)
if x:
    print("\nYes, there is at least one match ")
else:
    print("\nNo Match")

# "{}" -  Exactly the specified number of occurrences - Example "ai{2}"
# Task 3 -
txt = "The rain in Spain falls mainly in the plain"
# check if the string contains 'a' followed by exactly two "l" characters
x = re.findall("al{2}", txt)

print('\n', x)
if x:
    print("\nYes, there is at least one match ")
else:
    print("\nNo Match")

# "|" - Either or - Example "falls|stays"
txt = "The rain in Spain falls mainly in the plain"
# check if the string contains either falls or stays
x = re.findall("fall|stays", txt)
print('\n', x)
if x:
    print("\nYes, there is at least one match ")
else:
    print("\nNo Match")

# "" -  - Example ""
print("Task 3 -")

# Task 4 -
print("Task 4 -")

# Task 5 -
print("Task 5 -")

# Task 6 -
print("Task 6 -")

# Task 7 -
print("Task 7 -")

# Task 8 -
print("Task 8 -")

# Task 9 -
print("Task 9 -")

# Task 10 -
print("Task 10")

# Task 11 -
print("Task 11")

# Task 12 -
print("Task 12")

# Task 13 -
print("Task 13")

# Task 14 -
print("Task 14")

# Task 15 -
print("Task 15")

# Task 16 -
print("Task 16")

# Task 17 -
print("Task 17")
