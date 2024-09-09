# Collision Handling 

# Collision occurs when two keys hash to the same index. There are several strategies to handle collisions:
# 1. Open Hashing (Separate Chaining)
# 2. Linear Probing
# 3. Double Hashing

# Part 1: Open Hashing (Separate Chaining)
# Open Hashing stores all elements that hash to the same slot into a list at that slot.

class OpenHashingHashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)]

    def hash_function(self, key):
        return key % self.table_size

    def insert(self, key):
        """Inserts a key into the hash table using open hashing."""
        hash_index = self.hash_function(key)
        self.hash_table[hash_index].append(key)

    def search(self, key):
        """Searches for a key in the hash table."""
        hash_index = self.hash_function(key)
        return key in self.hash_table[hash_index]

# Part 2: Linear Probing
# Linear Probing handles collisions by moving to the next available slot in the array.

class LinearProbingHashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def hash_function(self, key):
        return key % self.table_size

    def insert(self, key):
        """Inserts a key into the hash table using linear probing."""
        hash_index = self.hash_function(key)
        while self.hash_table[hash_index] is not None:
            hash_index = (hash_index + 1) % self.table_size
        self.hash_table[hash_index] = key

    def search(self, key):
        """Searches for a key in the hash table."""
        hash_index = self.hash_function(key)
        while self.hash_table[hash_index] is not None:
            if self.hash_table[hash_index] == key:
                return True
            hash_index = (hash_index + 1) % self.table_size
        return False

# Part 3: Double Hashing
# Double Hashing uses a second hash function to determine the probe step.

class DoubleHashingHashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def hash_function1(self, key):
        return key % self.table_size

    def hash_function2(self, key):
        return 1 + (key % (self.table_size - 1))

    def insert(self, key):
        """Inserts a key into the hash table using double hashing."""
        hash1 = self.hash_function1(key)
        hash2 = self.hash_function2(key)
        i = 0
        while self.hash_table[(hash1 + i * hash2) % self.table_size] is not None:
            i += 1
        self.hash_table[(hash1 + i * hash2) % self.table_size] = key

    def search(self, key):
        """Searches for a key in the hash table."""
        hash1 = self.hash_function1(key)
        hash2 = self.hash_function2(key)
        i = 0
        while self.hash_table[(hash1 + i * hash2) % self.table_size] is not None:
            if self.hash_table[(hash1 + i * hash2) % self.table_size] == key:
                return True
            i += 1
        return False

# Example Usage
# Initializing hash tables with different collision handling schemes
open_hashing_ht = OpenHashingHashTable(10)
linear_probing_ht = LinearProbingHashTable(10)
double_hashing_ht = DoubleHashingHashTable(10)

# Insert keys
for key in [21, 31, 41, 51, 61]:
    open_hashing_ht.insert(key)
    linear_probing_ht.insert(key)
    double_hashing_ht.insert(key)

# Search for a key
print("Open Hashing search for 31:", open_hashing_ht.search(31))
print("Linear Probing search for 31:", linear_probing_ht.search(31))
print("Double Hashing search for 31:", double_hashing_ht.search(31))

# Conclusion:
# Each collision handling scheme has its advantages and trade-offs.
# - Open Hashing (Separate Chaining) is simple but can lead to uneven distribution.
# - Linear Probing is easy to implement but suffers from clustering.
# - Double Hashing reduces clustering but requires more computation.
