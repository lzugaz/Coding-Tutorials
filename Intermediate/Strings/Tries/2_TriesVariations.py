# Tries Variations

# Understanding Tries Variations
# Tries are versatile, allowing for efficient string searches. Variations like Ternary Search Tries (TST) 
# and Suffix Tries optimize for specific use cases, such as substring search and memory efficiency.

# Part 1: Ternary Search Trie (TST) Representation
class TSTNode:
    """A node in a Ternary Search Trie."""
    def __init__(self, char):
        self.char = char  # The character stored in this node
        self.is_end_of_word = False  # True if this node marks the end of a word
        self.left = None  # Left child for characters less than this node's char
        self.middle = None  # Middle child for characters equal to this node's char
        self.right = None  # Right child for characters greater than this node's char

# TST Implementation focuses on flexible searching, especially useful for tasks like autocomplete, 
# where not all characters in a query string are known.

# Part 2: Suffix Trie Representation
# Suffix Tries are a specialized form of trie for fast substring, subsequence, and other pattern matching operations.
# Each node represents a suffix of a given string.

class SuffixTrieNode:
    """A node in a Suffix Trie."""
    def __init__(self):
        self.children = {}  # Each child represents a possible continuation of the suffix

class SuffixTrie:
    """The Suffix Trie data structure."""
    def __init__(self, text):
        """Initializes a suffix trie from the given text."""
        self.root = SuffixTrieNode()
        self.text = text
        for i in range(len(text)):
            self._insert_suffix(text[i:])

    def _insert_suffix(self, suffix):
        """Inserts a suffix of the text into the trie."""
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTrieNode()
            node = node.children[char]

# Suffix Tries are particularly powerful for substring search, allowing for queries in O(m) time, 
# where m is the length of the search string.

# Example Usage: Demonstrating TST and Suffix Trie is omitted for brevity.
# Implementing full operations (insert, search) for TST and building a complete Suffix Trie 
# for a given text illustrates their respective strengths in different search operations.

# Conclusion:
# - Ternary Search Tries offer a balance between space efficiency and search speed, ideal for autocomplete systems.
# - Suffix Tries provide a robust structure for fast substring searches, at the cost of higher space consumption.
