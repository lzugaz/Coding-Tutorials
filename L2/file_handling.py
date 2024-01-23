#File handling

# 1. opening and closing Files 

# How to open File 
# open()

# what you can do after opening

# r(read), w(write), a(append), r+(read and write)

# How to close file

# close()


# 2. Reading from Files

# read entire file with read()
# read line by line using readline() and readlines()


# Reading an entire file

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
    
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 3. Writing to files
# When you write to file you can use write() and writelines()
        
# Writing to a file
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")

# Appending to a file
with open('output.txt', 'a') as file:
    file.write("Another line\n")





# Question 1: Sum of Numbers
# Read numbers from a file and calculate their sum.
# Each number is on a separate line in the file.
# Print the sum or write it to another file.
    
# Question 2: Filter Numbers 
#Read numbers from a file.
# Filter out numbers that greater than 5,000.
# Write the filtered numbers to a new file.
