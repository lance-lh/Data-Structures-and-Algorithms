# DFS
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    '''
    # 1. first solution
    res = [] # global

    def dfs(ans = []):
        # exist
        if len(ans) == len(nums):
            res.append(ans)
            return

        # condition
        for num in nums:
            if num not in ans:
                # back stacking paras change
                dfs(ans+[num])

    dfs()
    return res
'''

    # 2. second solution
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    if not nums:
        res.append(path)

    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


'''
    # 3. third solution
    import itertools

    res = []
    # return iterator
    per_nums = itertools.permutations(nums)
    for num in per_nums:
        res.append(list(num))
    return res
'''

# test
if __name__ == "__main__":
    nums = [1,2,3]
    print(permute(nums))