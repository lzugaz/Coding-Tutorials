# Bucket Sort

# Part 1: Understanding Bucket Sort
# Bucket sort is a distribution sort that works by arranging elements into several 'buckets' and then sorting these buckets individually.
# Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort.

# Part 2: How Bucket Sort Works
# - Create a number of buckets (empty lists).
# - Scatter: Go over the original array, putting each object in its appropriate bucket.
# - Sort each non-empty bucket.
# - Gather: Visit the buckets in order and put all elements back into the original array.

# Implementing Bucket Sort in Python
def bucket_sort(arr, bucket_size=5):
    """
    Sorts an array in ascending order using the bucket sort algorithm.

    :param arr: List of elements to be sorted.
    :param bucket_size: The maximum size that each bucket can hold.
    :return: The sorted list.
    """
    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    min_value, max_value = min(arr), max(arr)

    # Initialize buckets
    bucket_count = ((max_value - min_value) // bucket_size) + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for i in range(len(arr)):
        bucket_index = (arr[i] - min_value) // bucket_size
        buckets[bucket_index].append(arr[i])

    # Sort each bucket and place into output array
    arr.clear()
    for bucket in buckets:
        # A different sorting algorithm can be applied here
        sorted_bucket = sorted(bucket)
        arr.extend(sorted_bucket)

    return arr

# Part 3: Using Bucket Sort
# Example of sorting an array with Bucket Sort
example_array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

# Sort the array
sorted_array = bucket_sort(example_array)

# Print the sorted array
print("Sorted array is:", sorted_array)
# Output: Sorted array is: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]

# Part 4: Characteristics of Bucket Sort
# - Time Complexity: O(n + k) on average, where n is the number of items and k is the number of buckets.
# - Space Complexity: O(n * k) due to the extra space required for the buckets.
# - Stable: Bucket sort is stable if the algorithm used to sort individual buckets is also stable.

# Conclusion
# Bucket sort is useful when input is uniformly distributed over a range and there's a reasonable number of buckets that can be used.
# It's particularly useful for floating-point numbers distribution which is uniformly spread across the range.
