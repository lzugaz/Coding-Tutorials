# Hashing and Hash Functions

# Hashing is a technique used to uniquely identify a specific object from a group of similar objects.
# Hash functions are used in hashing to compute an index into an array in which an element will be inserted or searched.

# Part 1: Understanding Hash Functions
# A hash function takes an input (or 'key') and returns an integer value, the 'hash code', which is used as an index in a hash table.
# The effectiveness of a hash function is measured by its ability to distribute data evenly across the hash table's array.

# Example of a Simple Hash Function for Integers
def simple_hash(key, table_size):
    """
    A simple hash function for integers.

    :param key: The key to hash.
    :param table_size: The size of the hash table array.
    :return: The hash value of the key.
    """
    return key % table_size

# Part 2: Hash Function for Strings
# Since strings are more complex than integers, we need a method to convert them into integers.
# A common approach is to convert each character into its ASCII value, then combine these values.

def hash_string(s, table_size):
    """
    A hash function for strings.

    :param s: The string to hash.
    :param table_size: The size of the hash table array.
    :return: The hash value of the string.
    """
    total = 0
    for i in range(len(s)):
        total += ord(s[i]) * (i + 1)  # Multiply ASCII value by its position to ensure uniqueness
    return total % table_size

# Part 3: Dealing with Collisions
# Collisions occur when two keys hash to the same index. There are several methods to handle collisions:
# 1. Chaining: Store multiple elements at the same index using a more complex data structure (e.g., a linked list).
# 2. Open Addressing: Find another spot in the table by probing (linear or quadratic probing, double hashing).

# Part 4: Example Usage
# Let's create a small hash table for demonstration.

table_size = 10
keys_int = [15, 25, 35, 45]
keys_str = ["apple", "banana", "cherry", "date"]

# Hashing integers
hashed_ints = [simple_hash(key, table_size) for key in keys_int]
print("Hashed integers:", hashed_ints)

# Hashing strings
hashed_strs = [hash_string(key, table_size) for key in keys_str]
print("Hashed strings:", hashed_strs)

# Conclusion:
# Hash functions play a crucial role in data storage and retrieval processes, 
# optimizing search operations by efficiently mapping keys to specific locations in a hash table.
# Proper handling of collisions and a good hash function design are essential for maintaining the performance of hash tables.
