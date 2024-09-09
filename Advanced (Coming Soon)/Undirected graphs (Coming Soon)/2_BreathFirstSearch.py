# Breadth-First Search (BFS)

# Part 1: Understanding BFS in Graphs
# Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
# It starts at a selected node and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

# Part 2: Graph Representation
# An undirected graph can be represented using an adjacency list, where each node has a list of its adjacent nodes.

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}  # Initialize adjacency list

    def add_edge(self, u, v):
        """Adds an edge between vertices u and v."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Since it's an undirected graph, add edge in both directions

# Part 3: BFS Algorithm Implementation
    def bfs(self, start_vertex):
        """Performs BFS traversal starting from start_vertex."""
        visited = [False] * self.num_vertices  # Mark all vertices as not visited
        queue = []  # Initialize a queue for BFS

        # Mark the start vertex as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            # Dequeue a vertex from the queue and print it
            v = queue.pop(0)
            print(v, end=' ')

            # Get all adjacent vertices of the dequeued vertex v.
            # If an adjacent vertex has not been visited, mark it visited and enqueue it.
            for neighbour in self.adj_list[v]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

# Part 4: Example Usage
# Create a graph
g = Graph(5)  # 5 vertices numbered from 0 to 4
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Breadth First Traversal (starting from vertex 0):")
g.bfs(0)

# Conclusion:
# BFS is a key algorithm for traversing or searching a graph. It's particularly useful for finding the shortest path on unweighted graphs.
# This implementation showcases how BFS explores all neighbors at the current depth before moving to the nodes at the next depth level.
