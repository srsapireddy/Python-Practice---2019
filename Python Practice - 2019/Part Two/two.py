# Sequences and File Operators

"""
str = input("Enter your input")
print("Received input is: ",str)
"""

"""
name = input("Enter your name ")
age = input("Enter your age ")
print("Welcome ", name)
print("Your age is ", age)
print("After 5 years, your age will be: ", (int(age)+5))
"""

# -----------------------------------------------------------
# Files in the python
# Tasks
"""
1. Opening and Closing Files
2. Writing and Reading Files
3. Renaming and Deleting Files
"""

# Opening - There are different modes of opening a python file
# read only mode, write mode, write+ mode which creates the file if it dosent exists.
# All these are for the sake of protection of file.
"""
file_Object = open(file_name,[access_mode])
"""
# Different Access Modes
"""
r - Reading Only (Default)
rb - Reading only in binary format
r+ - Both reading and writing
rb+ - Both reading and writing in binary format
w - Writing only. It overwrites the file if the file exists.
wb - Writing only in binary format. Overwrites the files as well.
w+ - Writing only. Creates the file if dosent exist.

a - Open files for appending (Allows to add to the bottom of the file - Like Edit)
ab - Appending in binary format
a+ - Both appending and reading
ab+ - Both appending and reading in binary format
"""

# Writing Files
"""
file_object.write(string)
"""
# Read Method
"""
file_object.read([count])
count - Number of characters it will read at a time.
"""
# Renaming files
"""
os.rename(current_file_name, new_file_name)
"""
# Deleting Files
"""
os.remove(file_name)
"""

# Closing - To avoid the memory leak. Should close the file after opening or the data in the file will be stored inside the RAM.

# EXAMPLES
"""
import os
newfile = open("Edureka_py.txt","w+")

for i in range(1,10):
    newfile.write("\n Hello, welcome to Python:")
"""

"""
import os
newfile = open("Edureka_py.txt","r")

for i in range(1,10):
    print(newfile.read())
"""

"""
import os
os.rename("Edureka_py.txt","new.txt")
"""

"""
import os
os.remove("new.txt")
"""

# FILE OBJECT ATTRIBUTES
"""
import os
newfile = open("Edureka_py.txt","w+")
print(newfile.mode)
print(newfile.name)
# newfile.softspace --> It returns a boolean which is a 0 or 1. Whether a space character is needed to be printed before another value when using print statements.
"""

# File.seek() and File.tell()
"""
file.seek(offset[,from]) --> Searching for a particular thing in the file
file.tell() --> Gives current position of the file
"""

# EXERCISE
"""
import os
newfile = open("Edureka_py.txt","r")

newfile.seek(5)
print(newfile.read())
print(newfile.tell())
"""

# ----------------------------------------------------------------------------
# Sequences - Continuous collections of data type. Data which allows the different operations on them.
# Sequence Operations
"""
Concatenation - Gluing two things together
Repetition - Taking a sequence and sort of multiplying with a number
Membership Testing - To check if certain item is a member of the collection or not
Slicing - Taking out a portion from a sequence
Indexing - Indexing the items
"""

# EXAMPLES
"""
list = ["Hadoop", "Python", "Android"]
print(list[0])
print(list[0:2])
print(list[-1])
# Concatenation
print(list+ ["React","Angular","Data Science"])
# Repetition
print(list *3)
# Membership Testing
print("Hadoop" in list, "Angular" in list)
"""

# ------
# Types of sequences in python - Lists, Strings, Dictionaries, Tuples, Sets
list = ["Hadoop", "Python", "Android"]
list[1] = "Java"
print(list)
del(list[2])
print(list)