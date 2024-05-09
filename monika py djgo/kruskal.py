class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskals(graph, vertices):
    min_spanning_tree = []
    graph_edges = []

    for u in graph:
        for v, weight in graph[u].items():
            graph_edges.append((u, v, weight))

    graph_edges.sort(key=lambda x: x[2])  # Sort edges by weight

    disjoint_set = DisjointSet(vertices)

    for edge in graph_edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            min_spanning_tree.append((u, v, weight))
            disjoint_set.union(u, v)

    return min_spanning_tree

def main():
    graph = {}
    vertices = set()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v, w = input("Enter edge (u v w): ").split()
        w = int(w)
        u, v = int(u), int(v)
        vertices.add(u)
        vertices.add(v)

        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}

        graph[u][v] = w
        graph[v][u] = w

    min_spanning_tree = kruskals(graph, vertices)

    print("Minimum Spanning Tree:")
    total_weight = 0
    for edge in min_spanning_tree:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
        total_weight += edge[2]

    print("Total weight of the Minimum Spanning Tree:", total_weight)

if __name__ == "__main__":
    main()
