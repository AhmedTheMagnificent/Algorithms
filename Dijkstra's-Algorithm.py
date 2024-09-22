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
        
    def dijkstra(self, s):
        visited = set()
        distance = {x: float('INF') for x in self.graph}
        distance[s] = 0
        
        min_heap = [(0, s)]  # (distance, node)
        
        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            
            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    if new_dist < distance[neighbor]:
                        distance[neighbor] = new_dist
                        heapq.heappush(min_heap, (new_dist, neighbor))
        
        return distance

# Example usage
g = Graph()
g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 4)
g.addEdge('B', 'C', 2)
g.addEdge('B', 'D', 5)
g.addEdge('C', 'D', 1)

distances = g.dijkstra('A')
print(distances)
