# Heap Construction

# Building a heap can be achieved through two primary methods: insertions and bottom-up heap construction.
# This tutorial covers both methods and explains their differences and applications.

# Part 1: Building a Heap through Insertions
# Insertion-based heap construction involves starting with an empty heap and inserting elements one by one.
# Each insertion is followed by a "heapify-up" process to maintain the heap property.

class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            # Swap the current element with its parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

# Part 2: Bottom-Up Heap Construction
# Bottom-up heap construction involves creating a heap from an unsorted array in linear time.
# This method does not use insertions. Instead, it starts from the lowest non-leaf nodes and applies "heapify-down" operations.

    def build_heap(self, arr):
        self.heap = arr
        # Start from the last non-leaf node and heapify down each node
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Compare with left child
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        # Compare with right child
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest element is not the parent
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

# Part 3: Insertions vs. Bottom-Up Construction
# - Insertions are useful when building a heap dynamically as elements arrive.
# - Bottom-up construction is more efficient for building a heap from a static, unsorted array, with O(n) time complexity.

# Example Usage
heap = Heap()
# Building heap through insertions
for key in [3, 2, 15, 5, 4, 45]:
    heap.insert(key)
print("Heap after insertions:", heap.heap)

# Building heap through bottom-up construction
unsorted_array = [3, 2, 15, 5, 4, 45]
heap.build_heap(unsorted_array)
print("Heap after bottom-up construction:", heap.heap)

# Conclusion
# Both insertion-based and bottom-up heap construction methods have their use cases.
# Choosing the right approach depends on the specific requirements of the application and the nature of the input data.
