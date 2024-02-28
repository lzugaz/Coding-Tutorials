# Selection Sort
# Part 1: Understanding Selection Sort
# Selection Sort is a simple comparison-based sorting algorithm. It divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list, and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.

# Part 2: How Selection Sort Works
# - Find the minimum element in the unsorted array.
# - Swap the found minimum element with the first element of the unsorted array.
# - Repeat the steps above for the remainder of the array (excluding the already sorted elements).

# Implementing Selection Sort in Python
def selection_sort(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm.

    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Part 3: Using Selection Sort
# Example of sorting an array with Selection Sort
arr = [64, 25, 12, 22, 11]

# Sort the array
selection_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
# Output: Sorted array is: [11, 12, 22, 25, 64]

# Part 4: Characteristics of Selection Sort
# - Time Complexity: O(n^2) as there are two nested loops.
# - Space Complexity: O(1), it is an in-place sorting algorithm.
# - Not stable: Does not maintain the relative order of records with equal keys, but can be made stable with slight modifications.
# - Not adaptive: The run time is the same regardless of the initial order of the elements.

# Conclusion
# Selection Sort is an intuitive algorithm and useful for small datasets. It's less efficient for larger lists compared to more advanced algorithms like mergesort, quicksort, or heapsort. However, its simplicity and the fact that it minimizes the number of swaps makes it interesting for certain applications.
