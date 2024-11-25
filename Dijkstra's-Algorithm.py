import heapq

class Graph():
    def __init__(self):
        self.graph = {}
        
    def addEdge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
            
        self.graph[u][v] = w
        self.graph[v][u] = w
        
    def dijkstra(self, start):
        heap = []
        heapq.heappush(heap, (0, start))
        distances = {vertex : float("inf") for vertex in self.graph.keys()}
        distances[start] = 0
        while heap:
            currentDistance, currentVertex = heapq.heappop(heap)
            for neighbour, weight in self.graph[currentVertex].items():
                distance = weight + currentDistance
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(heap, (distance, neighbour))
        return distances
    
    
        

# Example usage
g = Graph()
g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 4)
g.addEdge('B', 'C', 2)
g.addEdge('B', 'D', 5)
g.addEdge('C', 'D', 1)

distances = g.dijkstra('A')
print(distances)
