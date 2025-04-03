import heapq

# Algoritmo de Dijkstra
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Algoritmo de Floyd-Warshall
def floyd_warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}
    
    for node in nodes:
        dist[node][node] = 0
    
    for u in graph:
        for v, w in graph[u].items():
            dist[u][v] = w
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Algoritmo de Warshall
def warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    reach = {i: {j: 0 for j in nodes} for i in nodes}
    
    for u in graph:
        for v in graph[u]:
            reach[u][v] = 1
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach

# Algoritmo de Kruskal
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    
    def kruskal(self):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        e = 0
        i = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        return result

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

dijkstra_result = dijkstra(graph, 'A')
floyd_warshall_result = floyd_warshall(graph)
warshall_result = warshall(graph)

kruskal_graph = Graph(4)
kruskal_graph.add_edge(0, 1, 10)
kruskal_graph.add_edge(0, 2, 6)
kruskal_graph.add_edge(0, 3, 5)
kruskal_graph.add_edge(1, 3, 15)
kruskal_graph.add_edge(2, 3, 4)
kruskal_result = kruskal_graph.kruskal()

print("Dijkstra:", dijkstra_result)
print("Floyd-Warshall:", floyd_warshall_result)
print("Warshall:", warshall_result)
print("Kruskal:", kruskal_result)
