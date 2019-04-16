# https://github.com/minsuk-heo/problemsolving/tree/master/graph
# the difference between bfs and dfs is that
# bfs use queue and dfs use stack

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex

# test
vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4),\
            (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
graphs = (vertexList, edgeList)
print(dfs(graphs, 0))