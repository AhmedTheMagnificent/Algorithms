class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append(v)
        self.edges[v].append(u)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend([neighbor for neighbor in self.edges[vertex] if neighbor not in visited])

# Example usage:
g = Graph()
g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('a', 'd')
g.add_edge('b', 'c')
g.add_edge('b', 'd')
g.add_edge('c', 'd')

print("BFS starting from vertex 'a':")
g.bfs('a')
