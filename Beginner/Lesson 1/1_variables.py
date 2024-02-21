# Python Variables: A Beginner's Guide

# Part 1: What is a Variable?

# In programming, a variable is used to store data that can be used and manipulated throughout your code.
# Think of a variable as a container for storing information.

# Part 2: Creating and Assigning Values to Variables

# Variables are created the moment you first assign a value to them. Python is dynamically typed, so you don't need to declare a variable's type.

name = "Alice"  # Creates a variable named 'name' and assigns the string "Alice" to it.
age = 30  # Creates a variable named 'age' and assigns the integer 30 to it.
is_student = True  # Creates a boolean variable 'is_student' and sets it to True.

# Printing variables to see their values.
print("Name:", name)
print("Age:", age)
print("Is a student:", is_student)

# Part 3: Variable Types

# Python has various data types including strings, integers, floating-point numbers, booleans, lists, tuples, sets, and dictionaries.

# String: A series of characters.
course = "Python Programming"
print("Course:", course)

# Integer: Whole numbers without a decimal point.
credits = 3
print("Credits:", credits)

# Float: Numbers with a decimal point.
average_grade = 85.5
print("Average Grade:", average_grade)

# Boolean: Represents True or False.
is_enrolled = True
print("Is Enrolled:", is_enrolled)

# List: An ordered collection of items.
colors = ["Red", "Green", "Blue"]
print("Colors:", colors)

# Tuple: Similar to a list, but immutable (cannot be changed).
dimensions = (1920, 1080)
print("Dimensions:", dimensions)

# Set: An unordered collection of unique items.
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers)

# Dictionary: A collection of key-value pairs.
student_info = {"name": "Alice", "major": "Computer Science"}
print("Student Info:", student_info)

# Part 4: Changing and Reassigning Variables

# Variables can be reassigned to new values, even of different types.
credits = "Three"  # Changing from integer (3) to string ("Three")
print("Credits:", credits)

# Part 5: Dynamic Typing

# Python allows for dynamic typing, meaning you can reassign variables to different data types.
is_enrolled = "Yes"  # Initially, this was a boolean, now reassigned to a string.
print("Is Enrolled:", is_enrolled)

# This tutorial provides a foundation for understanding and working with variables in Python.
# Mastering variables is crucial as they are the basic units of data storage in programming.
