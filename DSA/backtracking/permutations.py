# DFS
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    if not nums:
        res.append(path)

    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# test
nums = [1,2,3]
print(permute(nums))