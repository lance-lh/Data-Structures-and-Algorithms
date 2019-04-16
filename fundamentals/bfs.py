# https://blog.csdn.net/Violet_ljp/article/details/80556460
# https://www.youtube.com/watch?v=pcKY4hjDrxk
# https://github.com/minsuk-heo/problemsolving/tree/master/graph

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    # adjacency is the combination of array and linked list
    for edge in edgeList:
        # edge is each edgelist tuple
        # edge[0] is the vertex that leading the connection with other vertices
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    # the property of queue is FIFO

    # if queue is not empty
    while queue:
        # first pop out the queue value and regard it as the vertex of adjacencylist
        current = queue.pop()
        # find all nerghbors in adjacency list
        for neighbor in adjacencyList[current]:
            # use visitedList as flag to denote the neighbor access or not
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        # add queue's popped element to the final bfs spanning tree
        visitedList.append(current)
    return visitedList

# test
vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)
print(bfs(graphs, 0))