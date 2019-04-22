def combine(n, k):
    '''
    :param n: int
    :param k: int
    :return: List[List[int]]
    '''
    res = []
    dfs(range(1, n + 1), k, [], res)
    return res


def dfs(nums, k, path, res):
    if k == 0:
        res.append(path)
        return
    if len(nums) >= k:
        for i in range(len(nums)):
            dfs(nums[i + 1:], k - 1, path + [nums[i]], res)
    return


# test
n = 4
k = 2
print(combine(n, k))