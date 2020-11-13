# Python delete a file

import os

# Task 1 - To delete a file, you must import the OS module and it runs os.remove() function
print("\nTask 1 - To delete a file, you must import the OS module and it runs os.remove() function")
if os.path.exists("del.txt"):
    os.remove("del.txt")
else:
    print("File does not exist")

# Task 2 - Delete a folder
# Todo - make sure you creat the folder
print("\nTask 2 - delete a folder")
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    print("Folder has been deleted")
else:
    print("folder does not exit")
# Task 3 -
print("\nTask 3 -")

# Task 4 -
print("\nTask 4 -")

# Task 5 -
print("\nTask 5 -")

# Task 6 -
print("\nTask 6 -")
