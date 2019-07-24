# -*- coding:utf-8 -*-
'''
有一个整形数组A，请设计一个复杂度为O(n)的算法，算出排序后相邻两数的最大差值。

给定一个int数组A和A的大小n，请返回最大的差值。保证数组元素多于1个。

测试样例：
[1,2,5,4,6],5
返回：2
'''

# idea: bucket sort
class Gap:
    def maxGap(self, A, n):
        # write code here
        mi = min(A)
        ma = max(A)
        l = [[] for i in range(n + 1)]

        for i in A:
            l[((i - mi) * n) // (ma - mi)].append(i)

        res = 0
        i,j = 0,1
        while j < len(l):
            while l[j] == []:
                j += 1
            res = max(res, min(l[j]) - max(l[i]))
            i = j
            j += 1
        return res

# test
A = [1,2,5,4,6]
n = 5
print(Gap().maxGap(A,n))