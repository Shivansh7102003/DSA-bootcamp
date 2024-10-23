class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph

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

    def remove_vertex(self, vertex):
        """Remove a vertex and its edges from the graph."""
        if vertex in self.graph:
            # Remove the vertex from other vertices' adjacency lists
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            # Remove the vertex
            del self.graph[vertex]
        else:
            print(f"Vertex {vertex} not found.")

    def remove_edge(self, vertex1, vertex2):
        """Remove the edge between vertex1 and vertex2."""
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)  # For undirected graph
        else:
            print("One or both vertices not found.")

    def display(self):
        """Display the graph as an adjacency list."""
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")

# Example usage of the Graph class
if __name__ == "__main__":
    g = Graph()

    # Adding vertices
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)

    # Adding edges
    g.add_edge(0, 1)
    g.add_edge(1, 2)

    # Displaying the graph
    print("Graph:")
    g.display()

    # Removing an edge
    print("\nRemoving edge (1, 2)")
    g.remove_edge(1, 2)
    g.display()

    # Removing a vertex
    print("\nRemoving vertex 1")
    g.remove_vertex(1)
    g.display()
