# Exception Handling

# Part 1: Understanding Exceptions
# Exceptions are errors detected during execution that can cause your program to crash if not handled properly.

# Example: ZeroDivisionError occurs when dividing by zero.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Attempted to divide by zero.")
# This try-except block catches the ZeroDivisionError and prints a custom message instead of crashing the program.

# Part 2: Catching Multiple Exceptions
# A single try block can catch multiple exceptions, allowing for specific responses to different error types.

try:
    # Potential code that can raise multiple types of exceptions
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except TypeError:
    print("Type error occurred.")
# This handles both ZeroDivisionError and TypeError by providing specific messages for each.

# Part 3: The Else Clause
# The else clause will execute if the try block does not raise an exception.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Division successful:", result)
# If no exceptions are raised in the try block, the else block is executed.

# Part 4: The Finally Clause
# The finally clause will execute no matter what, often used for cleanup actions.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This will execute regardless of what happens above.")
# The finally block executes after the try and except blocks, even if an exception is caught.

# Part 5: Raising Exceptions
# You can raise exceptions in Python to force an error condition.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Age is valid.")
        
try:
    check_age(-1)
except ValueError as e:
    print("ValueError caught:", e)
# This function checks if the age is negative and raises a ValueError if it is, which is then caught in the try-except block.

# Part 6: Custom Exceptions
# You can define your own exception types to handle specific error cases in your code.

class CustomError(Exception):
    """A custom exception class."""
    pass

try:
    raise CustomError("A custom error occurred.")
except CustomError as e:
    print(e)
# Custom exceptions allow for more flexible error handling and can be caught specifically using their class.

# Conclusion:
# Exception handling in Python is crucial for writing robust and error-resistant code. 
# By understanding and implementing try, except, else, finally blocks, and raising exceptions, you can manage errors more effectively.
# Practice with these concepts to enhance the reliability of your Python programs.
    