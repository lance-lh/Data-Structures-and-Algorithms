'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    def largestNumber(self, nums):
        '''
        :param nums: List[int]
        :return: str
        '''
        from functools import cmp_to_key
        # here, key is to achieve cmp (compare two adjacent elements in nums)
        res = ''.join(sorted(map(str, nums), key=cmp_to_key(lambda x,y: int(y+x)-int(x+y))))
        return res if res[0] != '0' else '0'

nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))