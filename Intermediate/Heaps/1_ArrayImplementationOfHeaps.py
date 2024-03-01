# Binary Heap (Array Implementation)

# Part 1: Understanding Binary Heaps
# A Binary Heap is a complete binary tree which satisfies the heap ordering property.
# The ordering can be one of two types: the min-heap or max-heap property.
# In a max-heap, for any given node I, the value of I is greater than or equal to the values of its children.
# An array A that represents a heap is an object with two attributes: A.length and A.heap-size.

# Part 2: Array Representation of a Heap
# - The root of the tree is A[0].
# - Given the index of a node, i, the indices of its parent, left child, and right child can be computed as follows:
#   - Parent(i) = (i - 1) // 2
#   - Left(i) = 2 * i + 1
#   - Right(i) = 2 * i + 2

# Implementing a Max-Heap in Python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.heapify_down(0)  # Restore the heap property
        return root

    def heapify_down(self, i):
        largest = i  # Initialize largest as root
        left = self.left(i)
        right = self.right(i)

        # See if left child of root exists and is greater than root
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # See if right child of root exists and is greater than root
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # Change root if needed
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # Swap
            self.heapify_down(largest)  # Heapify the root

# Part 3: Using the Max-Heap
# Example of using the max-heap with array implementation
max_heap = MaxHeap()
data = [3, 2, 15, 5, 4, 45, 10]

# Insert data into the heap
for item in data:
    max_heap.insert(item)

# Display the heap
print("Max-Heap array:", max_heap.heap)

# Extract maximum elements from the heap
print("Extract Max:", max_heap.extract_max())
print("Max-Heap array:", max_heap.heap)

# Part 4: Characteristics of Binary Heap Implemented with Array
# - Time Complexity of Insertion: O(log n) because we need to restore the heap property by comparing parent/child nodes and swapping.
# - Time Complexity of Extract Max: O(log n) due to the down-heap operation needed after removal.
# - Space Complexity: O(n) for storing n elements.

# Conclusion
# The array implementation of a binary heap is efficient and utilizes the nature of the complete binary tree to simplify index calculations.
# Heaps are particularly useful for priority queues, heap sort, and for building Huffman Trees.
