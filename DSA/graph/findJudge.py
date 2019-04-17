def findJudge(N, trust):
    '''
    :param N: int
    :param trust: List[List[int]]
    :return: int
    '''
    # if judge exists, it has N - 1 votes
    # we consider each person as a vertex and each trust relationship as a directed edge

    # note that: N is the num of people
    # N + 1 is the num of sub-list
    a = [0] * (N + 1)
    for i in trust:
        a[i[1]] += 1
        # why?
        a[i[0]] -= 1

    for j in range(1, len(a)):
        if a[j] == N - 1:
            return j

    return -1

# test
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(findJudge(N, trust))