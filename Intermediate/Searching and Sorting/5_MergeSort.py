# Merge Sort

# Part 1: Understanding Merge Sort
# Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm.
# Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

# Part 2: How Merge Sort Works
# - Divide: Divide the unsorted list into n sublists, each containing one element.
# - Conquer: Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.

# Implementing Merge Sort in Python
def merge_sort(arr):
    """
    Sorts an array in ascending order using the merge sort algorithm.

    :param arr: List of elements to be sorted.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the array elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        # Merging the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    """
    Merges two sorted sub-arrays into arr.

    :param arr: The original array.
    :param left_half: The left half sub-array.
    :param right_half: The right half sub-array.
    """
    i = j = k = 0

    # Copy data to temp arrays left_half[] and right_half[]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Part 3: Using Merge Sort
# Example of sorting an array with Merge Sort
example_array = [38, 27, 43, 3, 9, 82, 10]

# Sort the array
merge_sort(example_array)

# Print the sorted array
print("Sorted array is:", example_array)
# Output: Sorted array is: [3, 9, 10, 27, 38, 43, 82]

# Part 4: Characteristics of Merge Sort
# - Time Complexity: O(n log n) in all cases as the list is always divided into two halves and the merge operations take linear time.
# - Space Complexity: O(n), as it requires additional space for the temporary arrays.
# - Stable: Yes, as the merge operation does not change the relative order of elements.

# Conclusion
# Merge sort is an efficient and commonly used algorithm that is particularly good for large data sets. 
# It's especially suitable for sorting linked lists and large arrays where random access is costly.
