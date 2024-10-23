from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph as an adjacency list

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")

    def add_edge(self, vertex1, vertex2):
        """Add an edge between vertex1 and vertex2."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # For undirected graph
        else:
            print("One or both vertices not found.")

    def bfs(self, start_vertex):
        """Perform BFS starting from start_vertex."""
        if start_vertex not in self.graph:
            print(f"Vertex {start_vertex} not found in the graph.")
            return

        visited = set()  # Set to keep track of visited vertices
        queue = deque([start_vertex])  # Queue for BFS
        visited.add(start_vertex)

        print("BFS Traversal:", end=" ")

        while queue:
            current_vertex = queue.popleft()  # Dequeue a vertex
            print(current_vertex, end=" ")

            # Get all adjacent vertices of the dequeued vertex
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark it as visited
                    queue.append(neighbor)  # Enqueue it

# Example usage of the Graph class with BFS
if __name__ == "__main__":
    g = Graph()

    # Adding vertices
    for vertex in range(5):  # Adding vertices 0 to 4
        g.add_vertex(vertex)

    # Adding edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)

    # Perform BFS starting from vertex 0
    g.bfs(0)  
