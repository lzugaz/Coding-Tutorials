# Radix Sort

# Part 1: Understanding Radix Sort
# Radix Sort is a non-comparative integer sorting algorithm that groups numbers by their individual digits.
# It operates on the digits from least significant to most significant to sort the numbers.

# Part 2: How Radix Sort Works
# - Start by sorting the least significant digit using a stable sort (e.g., counting sort).
# - Continue sorting based on each subsequent significant digit.
# - After the last digit is sorted, the list is sorted.

# Implementing Radix Sort in Python
def counting_sort_for_radix(arr, exp):
    """
    Performs a counting sort based on the digit represented by exp.
    
    :param arr: List of elements to be sorted.
    :param exp: The exponent representing the digit's place value.
    """
    n = len(arr)
    output = [0] * n  # The output array that will have sorted arr
    count = [0] * 10  # Initialize count array as 0

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Main function to that sorts arr[] using Radix Sort
    
    :param arr: List of non-negative integer elements to be sorted.
    """
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed.
    # exp is 10^i where i is the current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Part 3: Using Radix Sort
# Example of sorting an array with Radix Sort
example_array = [170, 45, 75, 90, 802, 24, 2, 66]

# Sort the array
radix_sort(example_array)

# Print the sorted array
print("Sorted array is:", example_array)
# Output: Sorted array is: [2, 24, 45, 66, 75, 90, 170, 802]

# Part 4: Characteristics of Radix Sort
# - Time Complexity: O(nk), where n is the number of elements and k is the number of digits in the largest number.
# - Space Complexity: O(n + k), due to the auxiliary space used in the counting sort.
# - Non-comparative: Radix sort does not compare elements directly against each other.
# - Stable: A stable sorting algorithm is used for each digit, making the overall radix sort stable.

# Conclusion
# Radix sort is efficient for sorting large sets of data with a small number of digits. It is particularly useful when the range of array elements is not significantly larger than the number of elements.
