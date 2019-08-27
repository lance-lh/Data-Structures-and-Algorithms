'''
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

Example:

    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
'''


class Solution:
    def permuteUnique(self, nums):
        '''
        :param nums: List[int]
        :return: List[List[int]]
        '''
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # jump off this loop and continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

if __name__ == 'main':
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))

