# Introduction to Python Programming: Mastering Loops

# Part 1: Understanding the `for` Loop
# The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item.

# Example of a `for` loop iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# This loop prints each fruit in the fruits list.

# Part 2: The `range()` Function in `for` Loops
# The `range()` function generates a sequence of numbers, which can be used to repeat an action a specific number of times.

# Example of `for` loop with `range()`
for x in range(5):
    print(x)
# This prints numbers 0 to 4. Note: range(5) generates numbers from 0 up to but not including 5.

# Part 3: Understanding the `while` Loop
# The `while` loop repeats as long as a specified condition is true. It's used when the number of iterations is not known before the loop starts.

# Example of a `while` loop
count = 0
while count < 5:
    print(count)
    count += 1  # Important: Ensure the loop has a condition that will eventually be false, to avoid an infinite loop.

# Mimicking a `do-while` Loop in Python
# Python does not have a built-in `do-while` loop, but you can achieve similar functionality by using a `while` loop with a condition that always starts as true.

# Example of mimicking a `do-while` loop
count = 0
while True:  # Loop starts with a condition that's always true
    print(count)
    count += 1
    if count >= 5:
        break  # Exits the loop when count is 5

# Part 4: Loop Control Statements
# - `break`: Exit the loop.
# - `continue`: Skip the rest of the code inside the loop for the current iteration and move to the next iteration.
# - `pass`: Do nothing; it's used as a placeholder for future code.

# Example of `break` and `continue`
for x in range(10):
    if x == 3:
        continue  # Skip 3
    if x == 8:
        break  # Stop loop before reaching 8
    print(x)

# Conclusion on Loops
# `for` and `while` loops are powerful tools in Python, allowing you to automate and repeat tasks efficiently.
# Understanding how to control the flow of loops with `break`, `continue`, and `pass` adds flexibility to how you implement loops in your programs.
# Practice with these loop constructs and control statements to become comfortable using them in various programming scenarios.


