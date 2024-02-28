# File I/O

# Part 1: Opening and Reading Files
# To open a file, use the open() function. The 'r' mode is for reading.
# Example: Open a file named "example.txt" and print its contents.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# The 'with' statement ensures the file is properly closed after its suite finishes.

# Part 2: Reading Lines from a File
# To read each line of a file individually, you can use a loop.
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace.

# Part 3: Writing to Files
# Opening a file in 'w' mode allows writing. Note: This will overwrite the file if it exists.
with open('output.txt', 'w') as file:
    file.write("Hello, Python!\n")
# Use 'a' mode (append) instead of 'w' to add to the end of the file.

# Part 4: Appending to Files
# To add content to the end of an existing file without overwriting it, use 'a' mode.
with open('output.txt', 'a') as file:
    file.write("Appending a new line.\n")

# Part 5: Working with File Paths
# It's important to understand relative and absolute paths. os.path can be used for path manipulations.
import os
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# os.path.join() is used to build paths in a way that's independent of the operating system.
new_file_path = os.path.join(current_directory, 'newfile.txt')

# Part 6: Handling File I/O Errors
# Always handle potential I/O errors using try-except blocks.
try:
    with open('nonexistentfile.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

# Conclusion:
# This guide covers the basics of file handling in Python, including reading, writing, appending, and error handling.
# Practice with these examples to get comfortable with file operations in your Python projects.
# I made two files with random numbers, feel free to try some of this code out with these files.  
# The file names are "random.txt", which is just random numbers gernated, and "filtered_numbers.txt", which is numbers from 
# "random.txt" but filled by a random condition.
