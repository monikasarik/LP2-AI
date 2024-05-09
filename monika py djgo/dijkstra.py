import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # If graph is undirected

    def dijkstra(self, start):
        heap = [(0, start)]
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

if __name__ == "__main__":
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v, w = map(int, input("Enter edge (u v w): ").split())
        g.add_edge(u, v, w)

    start_vertex = int(input("Enter the starting vertex: "))
    distances = g.dijkstra(start_vertex)

    print("Shortest distances from vertex", start_vertex)
    for vertex, distance in distances.items():
        print("Vertex:", vertex, "Distance:", distance)
