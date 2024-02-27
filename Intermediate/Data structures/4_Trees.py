# Python Trees: A Beginner's Guide

# Part 1: Understanding Trees
# A tree is a hierarchical data structure consisting of nodes, where each node has a value and a list of references to other nodes (children).
# The top node is called the root, and nodes with no children are called leaves.

# Part 2: Basic Components of Trees
# - Node: Contains the data and references to child nodes.
# - Root: The top node from which all other nodes descend.
# - Parent and Child: In a tree, each node (except the root) has one parent and zero or more children.
# - Leaf: A node with no children.

# Defining a Tree Node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)  # Adds a child to this node

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]  # Removes a child from this node

# Part 3: Implementing a Simple Tree
# A basic tree structure where each node can have multiple children.

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def display(self, node, level=0):
        if node is not None:
            print(' ' * level * 4, node.data)  # Indent to represent the level of the node
            for child in node.children:
                self.display(child, level + 1)  # Recursive call to display children

# Part 4: Using the Tree
# Demonstrates how to create a tree and add nodes as children.

# Create the tree and add children
root_node = TreeNode("Fruits")
tree = Tree(root_node)

apple_node = TreeNode("Apple")
banana_node = TreeNode("Banana")
cherry_node = TreeNode("Cherry")

root_node.add_child(apple_node)
root_node.add_child(banana_node)
root_node.add_child(cherry_node)

# Adding a child to a child node
granny_smith_node = TreeNode("Granny Smith")
apple_node.add_child(granny_smith_node)

# Display the tree
print("Tree Structure:")
tree.display(tree.root)

# Part 5: Applications of Trees
# Trees are used in various applications, such as:
# - Managing hierarchical data, like file systems.
# - Implementing search trees and balanced trees for efficient searching and sorting.
# - Storing data for databases and indexing.
# - Supporting algorithms in network routing and AI.

# Conclusion
# Trees are a versatile and fundamental data structure in computer science, useful for representing hierarchical relationships and improving the efficiency of operations like search and sort.
