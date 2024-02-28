# Stack

# Part 1: What is a Stack?
# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.

# Part 2: Basic Operations
# - Push: Add an item to the top of the stack.
# - Pop: Remove the item from the top of the stack.
# - Peek/Top: Return the top element of the stack without removing it.
# - isEmpty: Check if the stack is empty.

# Part 3: Implementing a Stack in Python
# Python's list can be used to implement a stack.

class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items.

    def is_empty(self):
        return not self.items  # Check if the stack is empty.

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack.

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove the item from the top of the stack.
        else:
            return "Stack is empty"  # Return message if stack is empty.

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top element of the stack.
        else:
            return "Stack is empty"  # Return message if stack is empty.

    def size(self):
        return len(self.items)  # Return the size of the stack.

# Part 4: Using the Stack
# Demonstration of basic stack operations.

# Create a stack instance
my_stack = Stack()

# Push items onto the stack
my_stack.push('Apple')
my_stack.push('Banana')
my_stack.push('Cherry')

# Peek at the top item
print(f"Top item: {my_stack.peek()}")  # Output should be 'Cherry'

# Pop an item from the stack
print(f"Popped item: {my_stack.pop()}")  # Output should be 'Cherry'

# Check if the stack is empty
print(f"Is the stack empty? {my_stack.is_empty()}")  # Output should be False

# Get the size of the stack
print(f"Stack size: {my_stack.size()}")  # Output should be 2

# Part 5: Real-world Applications of Stacks
# Stacks are used in various applications such as:
# - Undo mechanisms in text editors.
# - Function call management in programming languages.
# - Syntax parsing in compilers and calculators.
# - Backtracking algorithms, like maze solving and puzzle games.

# Conclusion
# Stacks are a fundamental data structure with various applications in computer science and programming.
