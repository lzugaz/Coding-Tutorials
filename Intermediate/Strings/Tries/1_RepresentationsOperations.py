# Representations and Operations

# Part 1: Understanding Tries
# A Trie is a tree-like data structure that stores a dynamic set of strings, where the keys are usually strings.
# Unlike a binary search tree, no node in the trie stores the key associated with that node.
# Instead, its position in the trie defines the key with which it is associated.

# Part 2: Node Representation in Tries
class TrieNode:
    """A single node in the Trie."""
    def __init__(self):
        self.children = {}  # Dictionary to hold child nodes
        self.is_end_of_word = False  # True if node represents the end of a word

# Part 3: Trie Implementation
class Trie:
    """The Trie data structure."""
    def __init__(self):
        self.root = TrieNode()

    # Insertion Operation
    def insert(self, word):
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new TrieNode as child if char not present
            node = node.children[char]  # Move to the child node
        node.is_end_of_word = True  # Mark the end of a word

    # Search Operation
    def search(self, word):
        """Searches for a word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Character not found
            node = node.children[char]  # Move to the child node
        return node.is_end_of_word  # Check if current node marks the end of the word

    # Prefix Search Operation
    def starts_with(self, prefix):
        """Returns True if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Prefix exists in trie

# Part 4: Example Usage
trie = Trie()
words = ["apple", "app", "apricot", "bat", "batman", "batch", "bath"]
for word in words:
    trie.insert(word)

# Search for words
search_terms = ["apple", "bat", "bath", "bad", "appetizer"]
for term in search_terms:
    print(f"Search for '{term}':", trie.search(term))

# Search for prefixes
prefixes = ["app", "bat", "ba", "z"]
for prefix in prefixes:
    print(f"Prefix search for '{prefix}':", trie.starts_with(prefix))

# Conclusion:
# Tries are efficient for search operations, especially for prefix searches and auto-complete features.
# They offer quick insertion and search operations, making them ideal for applications involving large datasets of strings.
