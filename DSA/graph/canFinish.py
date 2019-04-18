def canFinish(numCourses, prerequisites):
    """
    :type numCourse: int
    :type prerequirements: List[List[int]]
    :rtype:bool
    """

    '''
    if not prerequisites:
        return True

    L = []

    from collections import defaultdict

    in_degrees = defaultdict(int)
    graph = defaultdict(list)
    # Construct the graph
    # try to construct a DAG using graph
    # store id in in_degrees
    for u, v in prerequisites:
        graph[v].append(u)
        in_degrees[u] += 1

    # fetch vertex with id = 0
    Q = [u for u in graph if in_degrees[u] == 0]

    while Q:  # while Q is not empty
        start = Q.pop()  # remove a node from Q

        L.append(start)  # add n to tail of L

        for v in graph[start]:  # for each node v with a edge e
            in_degrees[v] -= 1  # remove edge
            if in_degrees[v] == 0:
                Q.append(v)
    # check there exist a cycle
    for u in in_degrees:  # if graph has edge
        if in_degrees[u]:
            return False
    return True
    '''

    if not prerequisites:
        return True

    L = []

    # use list to assign numCourses id
    in_degrees = [0 for _ in range(numCourses)]
    graph = [[] for _ in range(numCourses)]
    # Construct the graph
    # try to construct a DAG using graph
    # store id in in_degrees
    for u, v in prerequisites:
        graph[v].append(u)
        in_degrees[u] += 1

    # fetch vertex with id = 0
    Q = [i for i in range(len(in_degrees)) if in_degrees[i] == 0]

    while Q:  # while Q is not empty
        start = Q.pop()  # remove a node from Q

        L.append(start)  # add n to tail of L

        for v in graph[start]:  # for each node v with a edge e
            in_degrees[v] -= 1  # remove edge
            if in_degrees[v] == 0:
                Q.append(v)
    # check there exist a cycle
    for u in in_degrees:  # if graph has edge
        if in_degrees[u]:
            return False
    return True

# test
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
canFinish(numCourses, prerequisites)