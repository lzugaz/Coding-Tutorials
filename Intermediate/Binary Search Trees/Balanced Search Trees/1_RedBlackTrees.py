# Part 1: Red-Black Tree Properties
# 1. Every node is either red or black.
# 2. The root is always black.
# 3. Red nodes can't have red children (No two red nodes can be adjacent).
# 4. Every path from root to NULL leaves has the same number of black nodes.
# 5. New insertions are always red.

# Node Definition for Red-Black Tree
class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="black")  # Sentinel node for leaves
        self.root = self.NIL

    # Part 2: Left Rotate
    def left_rotate(self, x):
        # x's right child takes x's position in the tree, and x becomes left child of its original right child
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Part 3: Right Rotate
    def right_rotate(self, x):
        # Symmetrical to left_rotate
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Part 4: Insertion
    def insert(self, data):
        # Standard BST insert
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent == None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "red"
        new_node.left = self.NIL
        new_node.right = self.NIL

        # Fix the tree in case any of the red-black properties have been violated
        self.insert_fixup(new_node)

    # Part 5: Insert Fixup
    def insert_fixup(self, node):
        """
        Fixes the RBT after insertion to maintain its properties.
        This method corrects the coloring and performs rotations as needed.
        """
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:  # Parent is the left child
                uncle = node.parent.parent.right  # Uncle node
                if uncle.color == "red":  # Case 1: Uncle is red
                    # Recolor parent and uncle to black, grandparent to red
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:  # Uncle is black
                    if node == node.parent.right:  # Case 2: Node is right child
                        # Perform left rotation on parent
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3: Node is left child
                    # Recolor and perform right rotation on grandparent
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:  # Symmetric to the above
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"  # Ensure the root is always black


# Part 6: Example Usage
rbt = RedBlackTree()
rbt.insert(55)
rbt.insert(40)
rbt.insert(65)
rbt.insert(60)
rbt.insert(75)
rbt.insert(57)

# The insert_fixup function is crucial and involves several cases to check and appropriately balance the tree
# by rotations (left_rotate and right_rotate) and changing node colors to maintain Red-Black Tree properties.
