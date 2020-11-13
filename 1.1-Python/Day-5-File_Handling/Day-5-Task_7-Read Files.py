"""
File Handling
Python File Handling
Python Read Files
Python Write/Create Files
Python Delete Files
"""  # https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&ab_channel=CoreySchafer

# Task 1 - File handling
# The key function for working with files in Python is the open() function
# The open() function takes two parameters, filename and mode
"""
There are four different (modes) for opening a file 


'r' - Read - Default value. Opens for a file for reading, error   
'a' - Append  - open the file for appending, creates the file if does not exist  
'w' - Write - Opens a file for writing, creates the file if does not exist   
'x' - Create - Creates the specified file, returns an error if the file exits  

In addition you can specify if the file should be handled as binary or text mode
't' - Text - Default value. Text mode   
'b' - Binary - Binary Mode (e.g. images)  
"""

print("\nTask 1 - Reading the file")
my_file = open("demofile.txt", 'r')
print(my_file.read())

# if the file is located in a different location, you have to specify the file path.
# Task 2 -
print("\nTask 2 - Reading the file")
my_file = open("/Users/thomasacton/Documents/Projects/Data_science/1.1-Python/Day-5-File_Handling/demofile.txt", 'r')
print(my_file.read())

# Task 3 - Read only parts of the file
print("\nTask 3 - Read only parts of the file")
my_file = open("demofile.txt", 'r')
print(my_file.read(5))  # read the first 5 characters

# Task 4 - Read line
# You can return one line by using the readline() method
print("\nTask 4 -")
my_file = open("demofile.txt", 'r')
print(my_file.readline())

# Task 5 - By calling readline() two times, you can read the two first lines
print("\nTask 5 -")
my_file = open("demofile.txt", 'r')
print(my_file.readline())
print(my_file.readline())

# Task 6 - Loop through the file per line
print("\nTask 6 - Loop through the file per line")
my_file = open("demofile.txt", 'r')
for x in my_file:
    print(x)

# Task 7 - Close files
# It is a good practice to always close the file when you are done with it.
print("\nTask 7 -")
my_file = open("demofile.txt", 'r')
print(my_file.readline())
my_file.close()

# Task 8 -
print("\nTask 8 -")
