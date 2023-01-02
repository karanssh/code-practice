from collections import defaultdict, deque


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder
    
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent = edge[0]
        child = edge[1]
        graph[parent].append(child)
        inDegree[child] +=1 
    
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    
    while sources:
        vert = sources.popleft()
        sortedOrder.append(vert)
        for child in graph[vert]:
            inDegree[child] -=1
            if inDegree[child] == 0:
                sources.append(child)
    
    if len(sortedOrder) != vertices:
        # indicates cycle in a graph 
        return []
    
    return sortedOrder

def main():
    print(
        str(
            topological_sort(4, [[3,2], [3, 0], [2,0], [2,1]])
        )
    )

main()