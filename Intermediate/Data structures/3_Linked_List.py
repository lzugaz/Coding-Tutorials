# Python Linked List: A Beginner's Guide

# Part 1: What is a Linked List?
# A linked list is a linear data structure where each element (node) contains a reference (link) to the next node in the sequence.

# Part 2: Basic Components
# - Node: The basic unit of a linked list containing data and a link to the next node.
# - Head: The first node in a linked list.
# - Tail: The last node in a linked list, which points to None.

# Defining a Node class
class Node:
    def __init__(self, data=None):
        self.data = data  # Assign data
        self.next = None  # Initialize next as None

# Part 3: Implementing a Linked List
# A basic singly linked list where each node points only to the next node in the list.

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    def is_empty(self):
        return self.head is None  # Check if the list is empty

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

# Part 4: Using the Linked List
# Demonstration of basic linked list operations.

# Create a linked list instance
my_list = LinkedList()

# Append items to the list
my_list.append('Apple')
my_list.append('Banana')
my_list.append('Cherry')

# Display the list
print("Linked List:")
my_list.display()  # Output: Apple -> Banana -> Cherry -> None

# Search for an item in the list
print("Searching for 'Banana':", my_list.search('Banana'))  # Output: True
print("Searching for 'Grape':", my_list.search('Grape'))  # Output: False

# Part 5: Real-world Applications of Linked Lists
# Linked lists are used in various scenarios such as:
# - Implementing stacks, queues, and other abstract data types.
# - Dynamic memory allocation where the size of the data structure can grow or shrink at runtime.
# - Implementing hash tables, adjacency lists for graphs, and more.

# Conclusion
# Linked lists offer flexibility in data storage and management, making them a fundamental structure in computer science and programming.
