def findMinHeightTrees(n, edges):
    '''
    :param n: int
    :param edges: List[List[int]]
    :return: List[int]
    '''

    # create n empty set object
    tree = [set() for _ in range(n)]

    # u as vertex, v denotes neighbor vertices
    # set add method ensure no repeat neighbor vertices
    for u, v in edges:
        tree[u].add(v), tree[v].add(u)

    # q and nq are list
    # q save leaf node
    # nq is empty
    q, nq = [x for x in range(n) if len(tree[x]) < 2], []

    while True:
        for x in q:
            # check y in tree[x]
            for y in tree[x]:
                # delete x in tree[y]
                tree[y].remove(x)
                if len(tree[y]) == 1:
                    nq.append(y)
        # when nq is empty, quit the loop
        if not nq:
            break
        nq, q = [], nq
    return q

# test
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(findMinHeightTrees(n, edges))