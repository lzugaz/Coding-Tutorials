# Insertion Sort

# Part 1: Understanding Insertion Sort
# Insertion sort is a simple sorting algorithm that builds the final sorted list one item at a time. 
# It is much less efficient on large lists than more advanced algorithms such as quicksort or merge sort.

# Part 2: How Insertion Sort Works
# - Start by assuming that the first element is already sorted.
# - Take the next element and scan it backwards through the sorted portion (i.e., the elements to the left of it).
# - Shift all the elements in the sorted section that are greater than the element to the right.
# - Insert the element at the correct position.

# Implementing Insertion Sort in Python
def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    :param arr: List of elements to be sorted.
    """
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i-1  # Start comparing with the element left of i
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at after the element just smaller than it.
        arr[j + 1] = key

# Part 3: Using Insertion Sort
# Example of sorting an array with Insertion Sort
example_array = [22, 27, 16, 2, 18, 6]

# Sort the array
insertion_sort(example_array)

# Print the sorted array
print("Sorted array is:", example_array)
# Output: Sorted array is: [2, 6, 16, 18, 22, 27]

# Part 4: Characteristics of Insertion Sort
# - Time Complexity: O(n^2) in the average and worst case, O(n) in the best case.
# - Space Complexity: O(1), as it only requires a single additional memory space.
# - Adaptive: Efficient for (quite) small data sets and data sets that are already substantially sorted.
# - Stable: Does not change the relative order of elements with equal keys.

# Conclusion
# Insertion sort is an intuitive algorithm and has advantages such as simplicity and low overhead. 
# It's useful when sorting small arrays or when you have almost sorted data.
