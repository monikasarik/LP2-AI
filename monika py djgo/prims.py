from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        visited = set()
        min_spanning_tree = []
        total_weight = 0
        starting_vertex = next(iter(self.graph))  # Start from any vertex
        visited.add(starting_vertex)

        while len(visited) < len(self.graph):
            min_weight = float('inf')
            min_edge = None

            for u in visited:
                for v, w in self.graph[u]:
                    if v not in visited and w < min_weight:
                        min_weight = w
                        min_edge = (u, v, w)

            if min_edge:
                min_spanning_tree.append(min_edge)
                visited.add(min_edge[1])
                total_weight += min_edge[2]

        return min_spanning_tree, total_weight

    def regenerate_mst(self, mst_edges):
        regenerated_tree = []
        total_weight = 0

        for edge in mst_edges:
            u, v, w = edge
            regenerated_tree.append((u, v, w))
            total_weight += w

        return regenerated_tree, total_weight

if __name__ == "__main__":
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v, w = map(int, input("Enter edge (u v w): ").split())
        g.add_edge(u, v, w)

    min_spanning_tree, mst_weight = g.prim_mst()
    print("\nMinimum Spanning Tree:")
    for edge in min_spanning_tree:
        print(edge)

    print("\nWeight of Minimum Spanning Tree:", mst_weight)

    regenerate_choice = input("\nDo you want to regenerate the MST? (yes/no): ").lower()
    if regenerate_choice == 'yes':
        regenerated_tree, regenerated_weight = g.regenerate_mst(min_spanning_tree)
        print("\nRegenerated Minimum Spanning Tree:")
        for edge in regenerated_tree:
            print(edge)
        print("\nWeight of Regenerated Minimum Spanning Tree:", regenerated_weight)
