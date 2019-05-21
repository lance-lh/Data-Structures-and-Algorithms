class Solution:
    def maxProduct(self, nums):
        '''
        :param nums: List[int]
        :return: int
        '''
        res=curmax=curmin=nums[0]
        for i in nums[1:]:
            curmax, curmin = max(i, i*curmax, i*curmin), min(i, i*curmax, i*curmin)
            res = max(res, curmax)
        return res

# test
nums = [-4,-3,-2]
print(Solution().maxProduct(nums))