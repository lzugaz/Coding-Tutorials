# Finding Connected Components

# Part 1: Understanding Connected Components
# In an undirected graph, a connected component is a set of vertices that are all reachable from each other.
# Identifying connected components is useful in many applications, such as understanding the structure of networks.

# Part 2: Graph Representation
# We'll represent the graph using an adjacency list, where each node has a list of its adjacent nodes.

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}  # Initialize adjacency list

    def add_edge(self, u, v):
        """Adds an edge between vertices u and v."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph, add edge in both directions

# Part 3: DFS for Exploring Connected Components
    def dfs(self, v, visited):
        """Depth First Search to mark all vertices reachable from v."""
        visited[v] = True  # Mark the current node as visited
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited)

    def find_connected_components(self):
        """Finds and prints all connected components in the graph."""
        visited = [False] * self.num_vertices  # Mark all vertices as not visited
        components = []  # To store the connected components

        for v in range(self.num_vertices):
            if not visited[v]:
                # If a vertex is not visited, start a new component from it.
                component = []
                self.dfs_collect(v, visited, component)
                components.append(component)

        return components

    def dfs_collect(self, v, visited, component):
        """DFS utility to collect all vertices belonging to the current connected component."""
        visited[v] = True
        component.append(v)  # Add vertex to current component
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.dfs_collect(neighbour, visited, component)

# Part 4: Example Usage
# Create a graph with 3 connected components
g = Graph(7)  # 7 vertices numbered from 0 to 6
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(5, 6)

connected_components = g.find_connected_components()

print("Connected Components:")
for i, component in enumerate(connected_components):
    print(f"Component {i+1}: {component}")

# Conclusion:
# This implementation demonstrates how to find and print all connected components in an undirected graph.
# It leverages DFS to explore the graph and identify sets of vertices that are reachable from each other,
# effectively grouping the graph's vertices into connected components.
