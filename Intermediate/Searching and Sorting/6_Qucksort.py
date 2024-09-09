# Quicksort
# Part 1: Understanding Quicksort
# Quicksort is an efficient divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

# Part 2: How Quicksort Works
# - Choose a pivot element from the array.
# - Reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position.
# - Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

# Implementing Quicksort in Python
def quicksort(arr):
    """
    Sorts an array in ascending order using the quicksort algorithm.

    :param arr: List of elements to be sorted.
    :return: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        # Partitioning phase
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        # Recursively sort the sublists
        return quicksort(less) + equal + quicksort(greater)

# Part 3: Using Quicksort
# Example of sorting an array with Quicksort
example_array = [3, 6, 8, 10, 1, 2, 1]

# Sort the array
sorted_array = quicksort(example_array)

# Print the sorted array
print("Sorted array is:", sorted_array)
# Output: Sorted array is: [1, 1, 2, 3, 6, 8, 10]

# Part 4: Characteristics of Quicksort
# - Time Complexity: O(n log n) on average, O(n^2) in the worst case when the smallest or largest element is always chosen as the pivot.
# - Space Complexity: O(log n) because quicksort is applied recursively to sublists.
# - Not stable: The relative order of equal sort items is not preserved.
# - In-place: No additional space is needed except for recursive function calls.

# Conclusion
# Quicksort is a very efficient sorting algorithm, particularly for large datasets, 
# and is often faster in practice than other O(n log n) algorithms, 
# partially because its inner loop can be efficiently implemented on most architectures.
