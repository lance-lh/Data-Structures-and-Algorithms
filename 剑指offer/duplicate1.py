# -*- coding:utf-8 -*-

'''
不修改数组,找出重复的数字
在一个长度为n+1的数组里的所有数字都在1到n的范围内。
所有数组中至少有一个重复,请找出数组中任意一个重复的数字,
但不能修改输入的数组.例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7}，
那么对应的输出是重复的数字2或3。
'''

# 思路: 二分查找

class Solution:
    def duplicate(self, nums):
        if not nums:
            return -1
        m = len(nums)
        start = 1
        end = m - 1
        while start <= end:
            mid = (start + end) // 2
            count = self.countRange(nums,m,start,mid)

            if end == start:
                if count > 1:
                    return start
                else:
                    # quit the loop and return -1
                    break
            # start to middle
            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1

        return -1

    def countRange(self, nums,m,start, end):
        cnt = 0
        for i in range(m):
            if nums[i] >= start and nums[i] <= end:
                cnt += 1
        return cnt


# test
a = [2,3,5,4,3,2,6,7]
print(Solution().duplicate(a))