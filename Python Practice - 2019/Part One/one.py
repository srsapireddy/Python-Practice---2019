# Hello World
"""
print("Hello World")
print("Hello World")
print("Welcome to Edureka")
print("Happy Learning \nWelcome to Python") # New line character
"""
# ---------------------------------------------------------------
# Variables
"""
A = 10
B = "edureka!"

print(A,B)

x,y,z = 10,20,30
print(x)
print(y)
print(z)
"""

# ----------------------------------------------------------------
# Identifiers - Identifies a particular name for us
"""
a = 1
a0 = 1
0a = 1
A0 = 1
0A = 1
_a = 1
__a = 1
"""
# variables cant start with the digits
# Python dosent allow special symbols
# Class - Starts with an upper case letter and all other identifiers starts with a lower case letters.

# There are reserved memory locations in computers to store the variables (Computers Memory - RAM)
# It is done when running the file

# ------------------------------------------------------------------
# Standard Data Types in Python - To say what kind of data the variable is.
# Types - Immutable (It cannot be changed), Mutable (It can be changed)
"""
Mutable - Lists, Dictionaries, Sets
Immutable - Numbers, Strings, Tuples
"""
# Integers
"""
A = 10
B = 10.65
C = 10+6j
D = 5 + 4j
print(D-C)
print(A,B,C)
"""

# ---------
# Strings - Python dosent have Characters

# ---------
# Tuple - Fixed list. Comes within paranthesis. Faster than Lists
"""
list = (1,2,3)
print(list)
print(list[0])
"""
# -------------
# Mutable Data Types
# Lists - Can store different types of data. Lists are slower than Tuples.
"""
A = []
B = [1,2,13,3.5,"edureka"]
print(A)
print(B)
print(B[1])
B[1] = "changed"
print(A)

C = [[1,2,3],4,"third element",(2,4,5)]
print(C)
print(C[3][2])
"""
# ------------
# Dictionaries - Have key value pairs
# Makes the data very readable. For developer readability
"""
A = {"Age":24,"Name":"John"}
print(A["Age"])
"""
# Keys have to be strings. Values can be anything.
# -------------
# Sets - Unordered collection of items
# Every element is unique
"""
A = {1,2,3,3}
print(A)
"""

# ------------------------------------------------------------
# Operators
# [1] Arithmetic
# Division
"""
a = 4/5
print(a)

# Modules
b = 4%5
print(b)

# Power
c = 2**3
print(c)

# Floor Division
d = 2//2.0
print(d)
"""

# [2] Assignment
# Assigns values form right to left
# Short hand notation
"""
a = 1
b = 1
a = a + b
print(a)
a += b
print(a)
"""

# [3] Comparison - Gives Bollean values
# ==, !=, >, <, >=, <=

# [4] Logical Operators - and (Returns lower value), or (Returns higher value), not (More related to binary logic than the python logic)

# Bitwise Operators - Done on Bits
# & (AND), |(OR), ^(XOR), ~(NOT), <<(LEFT SHIFT), >>(RIGHT SHIFT)

# Identity - Very readable
"""
print(5 is 4)
print(5 is not 4)
"""

# Membership - Checks if certain thing exists with in a certain thing
# Applies for dictionaries, lists and tuples
"""
list = (4,5,6)
print(4 in list)
"""

# ----------------------------------------------------------------------
# Conditional Statements - Used to execute a statement or a group of statements when some condition is true
# If statements
"""
X = 10
Y = 12

if(X<Y):
    print("X is less than Y")
elif(X>Y):
    print("X is greater than Y")
else:
    print("X and Y are equal")
"""

# if else statement
"""
a = 10
if(a<=10):
    print("Less than 10")
if(10<=a<=25):
    print("In between 10 and 25")
else:
    print("Greater than 25")
"""

# ----------------------------------------------------------------------
# Loops - To repeate the same things again and again if a condition is met n number of times
# [1] while - forms until an expression is true
"""
count = 0
while(count<5):
    print(count)
    count = count+1
print("Good bye!")
"""

"""
rank = 5
while(rank!=12):
    print("Rank is",rank)
    rank += 1
"""

# [2] For Loop - It iterates over a range (range could be a list, tuple or a dictionary) anything that is a collection.
"""
fruits = ["Banana","Apple","Grapes"]
for fruit in fruits:
    print(fruit)
"""

# Print factorial of a number (Using for loop) # -------------

# Nested Loops - Loops in side loops

# BANK ATM USING NESTED LOOPS # -----------------

# Loop Control Statements
"""
break statement - To terminate loop
continue statement - To skip the loop
pass statement - To define an empty body
"""
"""
for i in range(1,11):
    if i == 5:
        break
    print(i)
"""

# ------------------------------------------------------------------------
# Command line parameters
# When executing a python file we want to pass certain arguments to it.
# Have a built in module for it
# Module - Library in python
# sys module -> Stands for Operating System. It allows to access the arguments that we are passing.
# sys.argv --> List of command-line arguments
# len(sys.argv) ---> Number of command-line arguments

import sys

print(len(sys.argv))
print(sys.argv)
