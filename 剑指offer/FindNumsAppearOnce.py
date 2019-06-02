# -*- coding:utf-8 -*-

'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''


# hash table
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        from collections import Counter
        d = Counter(array)
        res = []
        for i in d:
            if d[i] == 1:
                res.append(i)
        return res
'''

# bit manipulation
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        # 异或
        tmp = 0
        for i in array:
            tmp ^= i
        # 找最低位1出现的index
        # ind from right to left
        ind = 0
        while tmp & 1 == 0:
            tmp >>= 1
            ind += 1
        # 分组异或
        a = b = 0
        for i in array:
            if self.isBit(i, ind):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def isBit(self, num, ind):
        num = num >> ind
        return num & 1

# test
nums = [1,1,4,5,6,7,4,7]
print(Solution().FindNumsAppearOnce(nums))