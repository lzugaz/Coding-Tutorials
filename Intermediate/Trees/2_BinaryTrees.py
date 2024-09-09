# Binary Trees

# Part 1: Understanding Binary Trees
# A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

# Part 2: Basic Components of Binary Trees
# - Node: The fundamental unit of a binary tree containing data, a left child, and a right child.
# - Root: The top node in a binary tree from which all nodes descend.
# - Leaf: A node with no children.

# Defining a Binary Tree Node
class TreeNode:
    def __init__(self, value):
        """
        Initialize a tree node.

        :param value: The value or data that the node holds.
        """
        self.value = value  # The data stored in the node
        self.left = None  # Reference to the left child
        self.right = None  # Reference to the right child

    def add_left_child(self, child_value):
        """
        Adds a left child to the current node.

        :param child_value: The value of the left child.
        """
        self.left = TreeNode(child_value)

    def add_right_child(self, child_value):
        """
        Adds a right child to the current node.

        :param child_value: The value of the right child.
        """
        self.right = TreeNode(child_value)

# Part 3: Traversing a Binary Tree
# Binary tree traversal methods include in-order, pre-order, and post-order traversals.

def in_order_traversal(node):
    """
    Traverse the binary tree in in-order sequence (left, root, right).

    :param node: The current node in the tree.
    """
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    """
    Traverse the binary tree in pre-order sequence (root, left, right).

    :param node: The current node in the tree.
    """
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    """
    Traverse the binary tree in post-order sequence (left, right, root).

    :param node: The current node in the tree.
    """
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

# Part 4: Using the Binary Tree
# Example of constructing a binary tree and performing traversals
root = TreeNode('A')
root.add_left_child('B')
root.add_right_child('C')
root.left.add_left_child('D')
root.left.add_right_child('E')
root.right.add_left_child('F')
root.right.add_right_child('G')

print("In-order Traversal:")
in_order_traversal(root)
print("\nPre-order Traversal:")
pre_order_traversal(root)
print("\nPost-order Traversal:")
post_order_traversal(root)

# Conclusion
# Binary trees are fundamental data structures used for hierarchical data representation and have various applications in computer science, such as in binary search trees, heaps, and more.
