# Graph Representations: Edge List, Adjacency List, and Adjacency Matrix

# Part 1: Understanding Graph Representations
# Graphs can be represented in several ways, each with its own advantages and disadvantages.
# The three common representations are Edge List, Adjacency List, and Adjacency Matrix.

# Edge List Representation
# An edge list represents a graph as an array of tuples (or arrays), where each tuple represents an edge connecting two nodes.

edge_list = [(0, 1), (1, 2), (2, 3), (3, 4)]  # Example edge list for a simple linear graph

# Advantages: Simple structure, easy to understand and implement.
# Disadvantages: Inefficient for queries like checking if an edge exists between two nodes.

# Part 2: Adjacency List Representation
# An adjacency list represents a graph as an array of lists. The index of the array represents a vertex
# and the list at each index stores the vertices that are adjacent to that vertex.

adjacency_list = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}  # Example adjacency list

# Advantages: Efficient in terms of space, especially for sparse graphs. Easy to iterate over all edges.
# Disadvantages: Can be less efficient for dense graphs compared to an adjacency matrix.

# Part 3: Adjacency Matrix Representation
# An adjacency matrix represents a graph using a 2D array. A value at row i and column j indicates
# the presence (and possibly the weight) of an edge between vertex i and vertex j.

adjacency_matrix = [
    [0, 1, 0, 0, 0],  # Node 0 is connected to Node 1
    [1, 0, 1, 0, 0],  # Node 1 is connected to Nodes 0 and 2
    [0, 1, 0, 1, 0],  # Node 2 is connected to Nodes 1 and 3
    [0, 0, 1, 0, 1],  # Node 3 is connected to Nodes 2 and 4
    [0, 0, 0, 1, 0]   # Node 4 is connected to Node 3
]  # Example adjacency matrix

# Advantages: Easy to understand and implement. Efficient for dense graphs and for operations like edge existence check.
# Disadvantages: Can be space-inefficient for sparse graphs, as it requires O(V^2) space.

# Example Usage and Operations
# Edge List: Finding all nodes connected to a given node can require traversing the entire list.
# Adjacency List: Easy to find all nodes connected to a given node by direct access.
# Adjacency Matrix: Checking if an edge exists between two nodes is an O(1) operation by checking the matrix value.

# Conclusion:
# The choice of graph representation depends on the specific needs of the application, 
# such as the type of graph operations that will be most common, and the expected density of the graph.
