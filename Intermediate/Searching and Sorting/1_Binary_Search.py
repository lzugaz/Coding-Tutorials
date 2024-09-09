# Binary Search
# Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed the possible locations to just one.

# Part 1: Understanding Binary Search
# Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array; if they are not equal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half until it is successful.

# Part 2: Basic Components
# Sorted Array: The prerequisite for binary search is that the array must be sorted.
# Target: The value that needs to be searched in the array.
# Left and Right Pointers: Markers to keep track of the portion of the array that is being searched.
# Implementing Binary Search in Python 

def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the target value.

    :param arr: A list of sorted elements.
    :param target: The value to search for.
    :return: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1  # Initialize left and right pointers

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        
        # Check if the target is at the mid
        if arr[mid] == target:
            return mid  # Target found
        
        # Decide which half to choose for continuing the search
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found

# Part 3: Using Binary Search
# Let's use binary search to find a target in a sorted list:

# Example sorted array
my_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Target value to find
target = 40

# Perform binary search
index = binary_search(my_array, target)

# Output the result
if index != -1:
    print(f"Target {target} found at index: {index}")
else:
    print(f"Target {target} not found in the array.")



# Part 4: Efficiency and Limitations
# Efficiency: Binary search is highly efficient for sorted arrays, with a time complexity of O(log n).
# Limitations: The main limitation of binary search is that it requires 
# the array to be sorted. It's not suitable for unsorted arrays without preprocessing.

# Part 5: Applications of Binary Search
# Binary search is used in various applications, such as:

# Searching in databases.
# Finding the square root of a number (binary search on floating-point numbers).
# In algorithms that require searching, such as finding the minimum or maximum element in a rotated sorted array.

# Conclusion
# Binary search is a fundamental algorithm in computer science, known for its efficiency in searching sorted arrays. 
# Understanding how to implement and apply binary search is crucial for solving 
# many problems that involve searching and sorting.






