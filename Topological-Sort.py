# def TopologicalSort():
    
    
class Graph():
    def __init__(self, V):
        self.V = V
        self.list = {i: [] for i in range(1, V + 1)}
        self.in_degree = {i: 0 for i in range(1, V + 1)}
        
    def addEdge(self, u, v):
        self.list[u].append(v)
        self.in_degree[v] += 1
        
    def DFS(self, start):
        stack = [start]
        visited = []
        while len(stack) != 0:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                print(node)
            for neighbour in self.list[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    
                    
g = Graph(4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.DFS(1)
print(g.in_degree)

