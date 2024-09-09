# Binary Search Tree

# Part 1: Binary Search Tree (BST) Introduction
# A BST is a binary tree where each node has a unique key and satisfies the condition:
# All keys in the left subtree of a node are less than the node's key,
# and all keys in the right subtree are greater than the node's key.

class BSTNode:
    """A node in the binary search tree."""
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    # Part 2: Insert Operation
    def insert(self, key, value=None):
        """Inserts a key-value pair into the tree."""
        if not self.root:
            self.root = BSTNode(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, current, key, value):
        if key < current.key:
            if current.left is None:
                current.left = BSTNode(key, value)
            else:
                self._insert_recursive(current.left, key, value)
        elif key > current.key:
            if current.right is None:
                current.right = BSTNode(key, value)
            else:
                self._insert_recursive(current.right, key, value)
        else:
            # Key already exists; update the value
            current.value = value

    # Part 3: Search Operation
    def search(self, key):
        """Searches for the value associated with a key."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None:
            return None
        elif key == current.key:
            return current.value
        elif key < current.key:
            return self._search_recursive(current.left, key)
        else:  # key > current.key
            return self._search_recursive(current.right, key)

    # Part 4: Delete Operation
    def delete(self, key):
        """Deletes a node with a given key from the tree."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return None
        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            # Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Node with two children: Get the inorder successor
            temp_val = self._min_value_node(current.right)
            current.key = temp_val.key
            current.value = temp_val.value
            current.right = self._delete_recursive(current.right, temp_val.key)
        return current

    def _min_value_node(self, node):
        """Helper function to find the node with the minimum key."""
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example Usage:
bst = BinarySearchTree()
bst.insert(50, "A")
bst.insert(30, "B")
bst.insert(70, "C")
bst.insert(20, "D")
bst.insert(40, "E")
bst.insert(60, "F")
bst.insert(80, "G")

print("Search for 40:", bst.search(40))
bst.delete(70)
print("After deleting 70, search for 80:", bst.search(80))

# Conclusion:
# This BinarySearchTree class provides efficient methods for inserting, searching, and deleting nodes.
# These operations allow the BST to maintain sorted order, making it a useful data structure for various applications.
