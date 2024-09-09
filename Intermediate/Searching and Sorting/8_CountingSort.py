# Counting Sort

# Part 1: Understanding Counting Sort
# Counting sort is a sorting technique based on keys between a specific range. 
# It works by counting the number of objects having distinct key values, and doing some arithmetic to calculate the position of each object in the output sequence.

# Part 2: How Counting Sort Works
# - Calculate the histogram of key frequencies (count of distinct elements).
# - Compute the starting index for each key based on the counts.
# - Copy the items into an output array based on their calculated positions.
# - The original array is then updated with the sorted order from the output array, making it in-place.

# Implementing Counting Sort in Python
def counting_sort(arr):
    """
    Sorts an array in ascending order using the counting sort algorithm.
    Note: This implementation assumes the input is an array of non-negative integers.

    :param arr: List of non-negative integer elements to be sorted.
    :return: The sorted list.
    """
    if not arr:
        return arr
    
    # Find the maximum element (k) in the array to determine the range of counts
    max_val = max(arr)
    
    # Initialize count array with all zeros
    count_arr = [0] * (max_val + 1)
    
    # Store the count of each element in count array
    for num in arr:
        count_arr[num] += 1
    
    # Modify count array by adding the previous counts (cumulative count)
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    
    # Output array that will have the sorted order
    output_arr = [0] * len(arr)
    
    # Build the output array by placing elements at their correct positions
    for num in reversed(arr):
        output_arr[count_arr[num] - 1] = num
        count_arr[num] -= 1
    
    # Copy the sorted elements back into the original array
    for i, num in enumerate(output_arr):
        arr[i] = num
    
    return arr

# Part 3: Using Counting Sort
# Example of sorting an array with Counting Sort
example_array = [4, 2, 2, 8, 3, 3, 1]

# Sort the array
sorted_array = counting_sort(example_array)

# Print the sorted array
print("Sorted array is:", sorted_array)
# Output: Sorted array is: [1, 2, 2, 3, 3, 4, 8]

# Part 4: Characteristics of Counting Sort
# - Time Complexity: O(n + k) where n is the number of elements in input array and k is the range of input.
# - Space Complexity: O(k) for the count array.
# - Stable: Counting sort is stable if the iteration through the input array is done in a stable manner.
# - Non-comparative: It doesn't compare elements against each other.

# Conclusion
# Counting sort is efficient if the range of input data (k) is not significantly greater than the number of objects to be sorted (n).
# It's not suitable for sorting data with large ranges or non-integer keys.
