# Introduction to Python Programming: Mastering `if` Statements

# Part 1: Understanding `if` Statements
# `if` statements are used for conditional execution in Python.
# They allow code to execute only when a specific condition is true.

# Example of a basic `if` statement
x = 10
if x > 5:
    # This block executes because x is indeed greater than 5.
    print("x is greater than 5")

# Part 2: The Role of Indentation in `if` Statements
# Indentation is crucial for defining the block of code that runs if the condition is true.

y = 2
if y < 5:
    # This line is indented and executes because y is less than 5.
    print("y is less than 5")  

# Part 3: Using Comparison Operators in Conditions
# Conditions can involve comparison operators like ==, !=, <, >, <=, >=.

a = 1
b = 1
if a == b:
    # This uses == to check if a is equal to b, which it is.
    print("a is equal to b")

# Part 4: Logical Operators in Conditions
# Use logical operators (and, or, not) to combine conditions.

age = 18
is_student = True
if age >= 18 and is_student:
    # Both conditions are true, so this message prints.
    print("Eligible for student discount")

# Part 5: `if` Statements with Boolean Values
# Boolean values (True, False) can be used directly in conditions.

has_license = True
if has_license:
    # This condition is directly checked without a comparison operator.
    print("Allowed to drive")

# Part 6: Common Mistakes to Avoid

# 1. Forgetting the colon at the end of the `if` statement.
# Correct: if condition:
# Incorrect: if condition

# 2. Incorrect indentation leads to errors or unexpected behavior.
# Each line in the block under an `if` statement should be indented.

# 3. Misusing = (assignment operator) instead of == (equality operator) in conditions.
# Use == when you want to check if two values are equal.


# Part 7: Understanding the `if-else` Statement
# The `if-else` statement allows for two paths of execution: one if the condition is true, and another if it's false.

# Example of an `if-else` statement
temperature = 20
if temperature > 25:
    print("It's a hot day")
else:
    # This block executes because the condition is false.
    print("It's not a hot day")

# Part 8: Using `if-elif-else` for Multiple Conditions
# The `if-elif-else` chain lets you check multiple conditions sequentially, executing different blocks for each condition.

# Example of an `if-elif-else` chain
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    # This block executes if all the above conditions are false.
    print("Grade: D or F")

# Tips for Using `if-elif-else` Chains
# 1. The `if` condition is checked first; if it's false, `elif` conditions are checked in order.
# 2. `else` is optional but useful for handling cases not covered by `if` and `elif`.
# 3. There can be multiple `elif` blocks, but only one `if` and one `else` block.

# Part 9: Best Practices for `if-elif-else`
# - Use `elif` instead of multiple `if` statements when conditions are mutually exclusive.
# - Ensure conditions are ordered logically, from most specific to most general.
# - Keep conditions simple for readability and maintainability.

# Conclusion on Conditional Statements
# Mastering `if`, `if-else`, and `if-elif-else` statements is crucial for controlling the flow of your Python programs.
# These conditional statements allow your programs to make decisions and respond differently to various inputs and situations.
# Practice creating conditional structures to become comfortable with incorporating them into your programs.

