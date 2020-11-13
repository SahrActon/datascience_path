# Python File Write
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Writ will overwrite any existing context

# Task 1 - Writing to an existing file
print("\nTask 1 - Writing to an existing file")
f = open("demofile.txt", "a")
f.write("\nNow the file there is more content.")
f.close()

# open and read the file after the appending
f = open("demofile.txt", 'r')
print(f.read())
f.close()

# Task 2 - Overwrite the content
print("\nTask 2 - Overwrite the content")
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content")
f.close()

# open and read the file after the appending
f = open("demofile.txt", 'r')
print(f.read())

# Task 3 - Creating a new file
# To create a new file in python, use the open() method, with one of the following parameters:
"""
'x' - Create - will create a file, returns an error if the file 
'a' - Append - will create a file
'w' - Write -  will create a file if the specified file does not exit
"""
print("\nTask 3 - Creating a new file")
f = open("myfile.txt", "x")

# create a new file if it does not exit
try:
    f = open("myfile.txt", "w")
except OSError as e:
    print("The file already exist", e)
finally:
    f.close()

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
