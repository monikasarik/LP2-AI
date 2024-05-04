def greedy_mst(graph, start):
    mst = []
    visited = set()
    visited.add(start)
    
    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        
        for node in visited:
            for neighbor, weight in graph[node]:
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (node, neighbor, weight)
                
        if min_edge:
            mst.append(min_edge)
            visited.add(min_edge[1])
        else:
            break
        
    return mst

graph = {
    'A':[('B',2),('D',5)],
    'B':[('A',2),('C',1),('D',3)],
    'C':[('B',1),('D',4)],
    'D':[('A',5),('B',3),('C',4)]
}

start_node = 'A'
mst = greedy_mst(graph, start_node)
print("Minimum Spanning Tree edges : ")
for edge in mst:
    print(edge)