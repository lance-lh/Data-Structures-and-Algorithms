def permuteUnique(nums):
    res = []
    nums.sort()
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)

    for i in range(len(nums)):
        # the goal of using continue is to delete some unnecessary parts
        # here, nums[i] == nums[i - 1] shows what sort method does
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

# test
nums = [1,1,2]
print(permuteUnique(nums))