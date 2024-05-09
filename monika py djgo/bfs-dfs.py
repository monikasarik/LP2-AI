from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        traversal = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                traversal.append(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex])

        return traversal

    def dfs_util(self, vertex, visited, traversal):
        visited.add(vertex)
        traversal.append(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, traversal)

    def dfs(self, start):
        visited = set()
        traversal = []
        self.dfs_util(start, visited, traversal)
        return traversal

# Example usage
graph = Graph()

n = int(input("Enter the number of edges: "))
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.add_edge(u, v)

start_node = input("Enter the start node: ")

print("BFS Traversal:", graph.bfs(start_node))
print("DFS Traversal:", graph.dfs(start_node))
