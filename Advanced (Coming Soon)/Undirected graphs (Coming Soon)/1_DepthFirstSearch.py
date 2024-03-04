# Depth-First Search (DFS)

# Part 1: Understanding DFS in Undirected Graphs
# Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
# The algorithm starts at the root node and explores as far as possible along each branch before backtracking.

# Part 2: Graph Representation
# For DFS, an undirected graph can be represented using an adjacency list, where each node stores a list of its neighbors.

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}  # Initialize adjacency list

    def add_edge(self, u, v):
        """Adds an undirected edge between vertices u and v."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph, add edge in both directions

# Part 3: DFS Algorithm Implementation
    def dfs_util(self, v, visited):
        """Utility function for DFS, marks visited nodes and calls recursively on neighbors."""
        visited[v] = True  # Mark the current node as visited
        print(v, end=' ')  # Print the visited vertex
        
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        """Performs DFS traversal starting from start_vertex."""
        visited = [False] * self.num_vertices  # Mark all vertices as not visited
        
        # Call the recursive helper function to print DFS traversal
        self.dfs_util(start_vertex, visited)

# Part 4: Example Usage
# Create a graph given in the above diagram
g = Graph(5)  # 5 vertices numbered from 0 to 4
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(1, 4)

print("Depth First Traversal (starting from vertex 2):")
g.dfs(2)

# Conclusion:
# DFS is a fundamental algorithm for searching or traversing graph data structures, useful in many applications 
# such as topological sorting, solving puzzles, and analyzing networks. The key idea is to explore as far as possible 
# along each branch before backtracking.
