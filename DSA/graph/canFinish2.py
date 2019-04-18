def findOrder(numCourses, prerequisites):
    """
    :type numCourse: int
    :type prerequirements: List[List[int]]
    :rtype:list
    """

    L = []

    in_degrees = [0 for _ in range(numCourses)]
    graph = [[] for _ in range(numCourses)]

    # Construct the graph
    for u, v in prerequisites:
        graph[v].append(u)
        in_degrees[u] += 1

    Q = [i for i in range(len(in_degrees)) if in_degrees[i] == 0]  # collect nodes without pre-edges

    while Q:  # while Q is not empty
        start = Q.pop()  # remove a node from Q
        L.append(start)  # add n to tail of L

        for v in graph[start]:  # for each node v with a edge e
            in_degrees[v] -= 1  # remove edge
            if in_degrees[v] == 0:
                Q.append(v)

    for i in range(len(in_degrees)):  # if graph has edge
        if in_degrees[i] > 0:  # 这里的in_degrees check是大于０
            return []
    return L

# test
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# numCourses = 1
# prerequisites = []
print(findOrder(numCourses, prerequisites))