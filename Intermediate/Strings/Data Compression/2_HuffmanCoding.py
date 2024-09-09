# Huffman Coding for Data Compression

# Part 1: Understanding Huffman Coding
# Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters,
# with shorter codes for more frequent characters. This process reduces the overall size of the data.

import heapq
from collections import defaultdict, Counter

# Part 2: Building the Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # Character
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child
        self.right = None  # Right child

    def __lt__(self, other):
        # Overriding the less than operator for PriorityQueue
        return self.freq < other.freq

def build_huffman_tree(text):
    """Builds the Huffman Tree for the given text."""
    # Count frequency of occurrence of each character in the text
    frequency = Counter(text)

    # Create a priority queue to hold the nodes of Huffman tree
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Combine nodes until there is only one node left in the queue
    while len(priority_queue) > 1:
        # Extract the two nodes with the lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with these two nodes as children
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add this node back to the priority queue
        heapq.heappush(priority_queue, merged)

    # The remaining node is the root of the Huffman Tree
    return priority_queue[0]

# Part 3: Generating Huffman Codes
def generate_huffman_codes(node, prefix="", code_map=None):
    """Generates Huffman codes for characters by traversing the Huffman Tree."""
    if code_map is None:
        code_map = {}

    if node is not None:
        # Leaf node, contains a character
        if node.char is not None:
            code_map[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

# Part 4: Example Usage
text = "this is an example for huffman encoding"
# Build Huffman Tree
root = build_huffman_tree(text)
# Generate Huffman Codes
huffman_codes = generate_huffman_codes(root)

print("Huffman Codes for characters in text:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

# Conclusion:
# Huffman coding optimizes data compression by using variable-length codes for characters based on their frequencies.
# Characters with higher frequencies get shorter codes, reducing the overall size of the data.
