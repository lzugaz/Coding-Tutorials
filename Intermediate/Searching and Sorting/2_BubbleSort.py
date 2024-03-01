# Bubble Sort

# Part 1: Understanding Bubble Sort
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

# Part 2: How Bubble Sort Works
# - Compare adjacent elements: For each pair of adjacent elements, we compare their values and swap them if the first one is greater than the second one.
# - Repeated passes: This process is repeated for multiple passes through the list until no swaps are needed, indicating that the list is sorted.

# Implementing Bubble Sort in Python
def bubble_sort(arr):
    """
    Sorts an array in ascending order using the bubble sort algorithm.

    :param arr: List of elements to be sorted.
    """
    n = len(arr)  # Number of elements in the array
    for i in range(n):
        # Track whether any swap is made in this pass
        swapped = False
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Compare the element with its next element
            if arr[j] > arr[j+1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

# Part 3: Using Bubble Sort
# Example of sorting an array with Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]

# Sort the array
bubble_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
# Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]

# Part 4: Characteristics of Bubble Sort
# - Time Complexity: O(n^2) in the average and worst case scenarios.
# - Space Complexity: O(1), as it requires only a constant amount of additional space.
# - Adaptive: Can be optimized to stop early if the list becomes sorted before making all the passes.
# - Stable: Maintains the relative order of records with equal values.

# Conclusion
# Bubble Sort is a simple sorting algorithm suitable for small datasets or as an educational tool to understand sorting mechanisms. However, it's inefficient for large datasets compared to more advanced sorting algorithms like quicksort or mergesort.
