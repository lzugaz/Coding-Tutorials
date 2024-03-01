# Heapsort   

# Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure.
# It works by transforming the list into a heap, then repeatedly extracting the maximum (for max-heap)
# or minimum (for min-heap) element and putting it at the end of the list.

# Part 1: Building the Heap
# The first step in heapsort is to build a max-heap from the input list.
# A max-heap is a complete binary tree where each node is greater than its children.

def heapify(arr, n, i):
    """
    Helper function to maintain the heap property.

    :param arr: List representation of the heap
    :param n: Size of the heap
    :param i: Index of the element to heapify
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the root
        heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Function to build a max-heap from an unsorted list.

    :param arr: List to be sorted
    """
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Part 2: Heapsort Algorithm
# Once the heap is built, the elements are repeatedly removed from the heap and placed in the sorted position.

def heapsort(arr):
    """
    Main function to sort an array using heapsort.

    :param arr: List to be sorted
    """
    n = len(arr)
    build_max_heap(arr)
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root to end
        heapify(arr, i, 0)

# Part 3: Using Heapsort
# Example of sorting an array with Heapsort
example_array = [12, 11, 13, 5, 6, 7]

# Sort the array
heapsort(example_array)

# Print the sorted array
print("Sorted array is:", example_array)
# Output: Sorted array is: [5, 6, 7, 11, 12, 13]

# Conclusion
# Heapsort is an efficient in-place sorting algorithm with time complexity of O(n log n).
# It's not stable but offers a good compromise between simple O(n log n) sort algorithms like mergesort and quicksort.
