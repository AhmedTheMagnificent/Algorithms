import heapq
import random

class Graph():
    def __init__(self):
        self.graph = {}
        self.MST = {}
        
    def addEdge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
            
        self.graph[u][v] = w
        self.graph[v][w] = w
        
    def primMST(self):
        anynode = random.randrange(1, len(self.graph))
        visited = {}
        heap = []
        print(self.graph.keys())
        
        
g = Graph()
g.addEdge(0, 1, 2)
g.addEdge(0, 3, 6)
g.addEdge(1, 3, 3)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 4)
g.primMST()