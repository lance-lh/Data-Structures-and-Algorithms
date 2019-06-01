# -*- coding:utf-8 -*-

'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
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

# test
nums = [1,1,4,5,6,7,4,7]
print(Solution().FindNumsAppearOnce(nums))