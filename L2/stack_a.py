# Answer to Question 2: Reverse a String

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

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ''
    while not stack.isEmpty():
        reversed_string += stack.pop()
    return reversed_string

# Example usage
original_string = "Hello"
reversed_string = reverse_string(original_string)
print(reversed_string)
