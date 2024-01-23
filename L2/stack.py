# Stack

# 1. Introduction to Stacks
# They are a data structure.
# They act as a LIFO(Last In Frst Out)

# 2. Basic Stack Operations
# Push: Adding an element to the top of the stack.
# Pop: Removing the top element of the stack.
# Peek or Top: Viewing the top element of the stack without removing it.
# isEmpty: Checking if the stack is empty.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Outputs 3
print(stack.peek()) # Outputs 2


# Question 1: Basic Operations
# What would the following code do.
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())


# Question 2:Reverse a String
# Make a fuction using a Stack that reverses
# a string. eg("Hello" into "olleh")