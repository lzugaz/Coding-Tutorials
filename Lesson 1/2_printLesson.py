# Introduction to Python Programming: Focusing on Print Statements

# Part 1: Understanding Print Statements

# The print function outputs information to the console. It's a way to see the results of your code immediately.

# Greeting the class
print("hello TDM 511")  
# This line prints a greeting message saying "hello TDM 511". 
# It's a simple text output that appears on the screen.

print("\n")  
# Prints a newline character, which moves the cursor to the next line. 
# It's useful for adding space between different print outputs for better readability.

# Welcome message for lab two
print("Welcome to lab two")  
# This command prints another message: "Welcome to lab two". 
# Like the first print statement, it's a straightforward way to display text.

# Part 2: Printing Variables and Concatenating Strings

name = "Lucas Ugaz"  # Assigning the string "Lucas Ugaz" to the variable 'name'.
major = "Computer Science"  # Assigning the string "Computer Science" to the variable 'major'.

print(name)  
# This prints the contents of the variable 'name', which is the string "Lucas Ugaz".

print(major)  
# Prints the contents of the variable 'major', i.e., "Computer Science".

print("Name: ", name)  
# Prints a string "Name: " followed by the value stored in the variable 'name'.
# The comma in the print statement automatically adds a space between "Name: " and the variable's value.

print(name + " - " + major)  
# Concatenates the strings contained in 'name' and 'major', separated by " - ", and prints the result.
# The '+' operator is used to join strings together before printing.

# Part 3: Basic Arithmetic Display

a = 5  # Assigns the number 5 to variable 'a'.
b = 6  # Assigns the number 6 to variable 'b'.

print(a + b)  
# Calculates the sum of 'a' and 'b', then prints the result, which is 11.
# This demonstrates how print can also output the result of arithmetic operations directly.

# Example Answers for Questions:

# Printing your name
print("Your Name Here")  
# Replace 'Your Name Here' with your actual name to print it to the console.
# It's a straightforward way to display text that you've specified.

# Printing the result of adding two numbers
print(5 + 7)  
# This statement directly prints the result of the arithmetic operation 5 + 7, which is 12.
# It showcases how to perform calculations and display their results in a single step.

# These comments provide a clear explanation of what each print statement in the script is doing,
# making it easier for beginners to understand how printing works in Python.

# Part 4: Printing Booleans

# A boolean value represents one of two states: True or False. It's commonly used for conditional testing.

is_student = True  # Assigns the boolean value True to the variable 'is_student'.
has_major = False  # Assigns the boolean value False to the variable 'has_major'.

print(is_student)
# This prints the boolean value stored in 'is_student'. 
# The output will be True, indicating the condition or state represented by 'is_student'.

print(has_major)
# Prints the boolean value stored in 'has_major'.
# The output will be False, reflecting the condition or state that 'has_major' represents.

# Booleans are often used in control flow (e.g., if statements) to execute different code paths based on certain conditions.

# Part 5: Printing Lists

# Lists in Python are used to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values.

courses = ["Math", "Science", "History", "English"]  # Creates a list of course names.
numbers = [1, 2, 3, 4, 5]  # Creates a list of numbers.

print(courses)
# This command prints the entire list 'courses' as it's stored, including brackets and quotes.
# The output will be: ['Math', 'Science', 'History', 'English']

print(numbers)
# Prints the entire list 'numbers'. 
# The output will be: [1, 2, 3, 4, 5], showing the list structure and the contained integers.

# It's also possible to print individual elements or a range of elements from a list.

print(courses[0])
# Prints the first element in the list 'courses', which is "Math".
# Lists are zero-indexed in Python, so the first element is accessed with index 0.

print(numbers[1:4])
# Prints a slice of the list 'numbers', starting from index 1 up to but not including index 4.
# The output will be: [2, 3, 4], which includes the second through the fourth numbers.

# This demonstration shows how to print various data types in Python, including booleans and lists.
# Understanding these basics is crucial for manipulating data and controlling the flow of your programs.
