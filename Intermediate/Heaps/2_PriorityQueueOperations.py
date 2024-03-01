# Priority Queue using Binary Heap

# A priority queue is an abstract data type where each element has a "priority" associated with it. 
# In a priority queue, an element with high priority is served before an element with low priority.
# This implementation focuses on using a binary heap to efficiently manage the priority queue operations.

# Part 1: Priority Queue Operations
# The primary operations of a priority queue are insertion and extracting the minimum or maximum element.
# - Insertion: Adds a new element to the priority queue while maintaining the heap structure.
# - Extract Min/Max: Removes and returns the element with the highest or lowest priority.

# Part 2: Binary Heap for Priority Queue
# A binary heap is a complete binary tree that can be either a min-heap or max-heap.
# - In a min-heap, the parent node has a lower value than its children, making the root the minimum element.
# - In a max-heap, the parent node has a higher value than its children, making the root the maximum element.
# Binary heaps are efficient for implementing priority queues because they allow both insertion and extraction operations in O(log n) time.

# Implementing Priority Queue
class PriorityQueue:
    def __init__(self, heap_type='min'):
        self.heap = []
        self.heap_type = heap_type  # 'min' for min-heap, 'max' for max-heap

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        if self.heap_type == 'min':
            while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
                self.swap(index, self.parent(index))
                index = self.parent(index)
        else:  # max-heap
            while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
                self.swap(index, self.parent(index))
                index = self.parent(index)

    def extract(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self.heapify_down(0)
        return root

    def heapify_down(self, index):
        smallest_or_largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if self.heap_type == 'min':
            if left < len(self.heap) and self.heap[left] < self.heap[smallest_or_largest]:
                smallest_or_largest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest_or_largest]:
                smallest_or_largest = right
        else:  # max-heap
            if left < len(self.heap) and self.heap[left] > self.heap[smallest_or_largest]:
                smallest_or_largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[smallest_or_largest]:
                smallest_or_largest = right

        if smallest_or_largest != index:
            self.swap(index, smallest_or_largest)
            self.heapify_down(smallest_or_largest)

# Part 3: Using the Priority Queue
# Create a priority queue and perform insertions and extraction
pq = PriorityQueue('min')  # Change to 'max' for a max-heap
pq.insert(3)
pq.insert(1)
pq.insert(4)
pq.insert(1)
pq.insert(5)

print("Extracting from priority queue:", pq.extract())  # For min-heap: 1, for max-heap: 5
print("Heap after extraction:", pq.heap)

# Conclusion
# The priority queue, implemented using a binary heap, provides efficient insertion and extraction.
# This data structure is vital for algorithms that require frequently updating priorities, like Dijkstra's shortest path algorithm.
