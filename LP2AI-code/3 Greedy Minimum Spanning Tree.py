def prim(graph, start):
    mst = [] 
    visited = set() 
    visited.add(start)
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]  # Store edges from the start node
    
    edges.sort()
    
    while edges:
        weight, src, dest = edges.pop(0)
        
        if dest not in visited:
            mst.append((src, dest, weight))
            visited.add(dest)
            
            for neighbor, weight in graph[dest]:
                if neighbor not in visited:
                    edges.append((weight, dest, neighbor))
                    edges.sort() 
    return mst

graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 4)],
    'D': [('A', 5), ('B', 3), ('C', 4)]
}

start_node = 'A'
mst = prim(graph, start_node)
print("Minimum Spanning Tree (MST) edges:")
for edge in mst:
    print(edge)