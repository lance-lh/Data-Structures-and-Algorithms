'''
Given an unsorted array of integers,
find the length of longest increasing subsequence.

Example:
    Input: [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:
    1. There may be more than one LIS combination, it is only necessary for you to return the length.
    2. Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

# binary search to find left boundary (similar to poker)
class Solution:
    def lengthOfLIS(self, nums):
        '''
        :param nums: List[int]
        :return: int
        '''
        # stack to indicate 牌的堆顶（覆盖存储）
        stack = [0] * len(nums)
        # 扑克牌堆数
        piles = 0

        for i in range(len(nums)):
            # current poker
            poker = nums[i]
            left, right = 0, piles
            # left boundary, [left,right)
            while left < right:
                mid = (left + right) // 2
                if stack[mid] == poker:
                    right = mid
                elif stack[mid] > poker:
                    right = mid
                else:
                    left = mid + 1
            # if no proper pile to put poker, create new one
            if left == piles:
                piles += 1
            # here, left indicate 找到的最左堆或者新建立的堆（left == piles）
            stack[left] = poker
        return piles



# dp with O(n^2) solution

# class Solution:
#     def lengthOfLIS(self, nums):
#         '''
#         :param nums: List[int]
#         :return: int
#         '''
#         # initialize dp with all 1,since it has 1 length itself
#         dp = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] < nums[j]:
#                     dp[i] = max(dp[i],dp[j]+1)
#         return max(dp)


# test
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))