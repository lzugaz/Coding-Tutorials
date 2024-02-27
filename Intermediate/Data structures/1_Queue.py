# Python Queue Data Structure: A Beginner's Guide

# Part 1: What is a Queue?
# A queue is a linear data structure that follows the First In, First Out (FIFO) principle.

# Part 2: Basic Operations
# - Enqueue: Add an item to the end of the queue.
# - Dequeue: Remove the item from the front of the queue.
# - Peek/Front: Return the front element of the queue without removing it.
# - isEmpty: Check if the queue is empty.
# - isFull: Check if the queue is full (for fixed-size queues).

# Part 3: Implementing a Queue in Python
# Python's list can be used to implement a queue, but collections.deque is preferred for efficient appends and pops from both ends.

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()  # Initialize a deque for storing queue items.

    def is_empty(self):
        return not self.items  # Check if the queue is empty.

    def enqueue(self, item):
        self.items.append(item)  # Add an item to the end of the queue.

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # Remove the item from the front of the queue.
        else:
            return "Queue is empty"  # Return message if queue is empty.

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Return the front element of the queue.
        else:
            return "Queue is empty"  # Return message if queue is empty.

    def size(self):
        return len(self.items)  # Return the size of the queue.

# Part 4: Using the Queue
# Demonstration of basic queue operations.

# Create a queue instance
my_queue = Queue()

# Enqueue items into the queue
my_queue.enqueue('Apple')
my_queue.enqueue('Banana')
my_queue.enqueue('Cherry')

# Peek at the front item
print(f"Front item: {my_queue.peek()}")  # Output should be 'Apple'

# Dequeue an item from the queue
print(f"Dequeued item: {my_queue.dequeue()}")  # Output should be 'Apple'

# Check if the queue is empty
print(f"Is the queue empty? {my_queue.is_empty()}")  # Output should be False

# Get the size of the queue
print(f"Queue size: {my_queue.size()}")  # Output should be 2

# Part 5: Real-world Applications of Queues
# Queues are used in various applications such as:
# - Managing tasks in operating systems.
# - Handling requests on web servers.
# - Implementing breadth-first search (BFS) algorithms.
# - Queueing systems for customer service or processing orders.

# Conclusion
# Queues are a versatile data structure with a wide range of applications in computer science, programming, and beyond.
