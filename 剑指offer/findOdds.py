# -*- coding:utf-8 -*-
'''
给定一个整型数组arr，其中有两个数出现了奇数次，其他的数都出现了偶数次，
找到这两个数。要求时间复杂度为O(N)，额外空间复杂度为O(1)。

给定一个整形数组arr及它的大小n，请返回一个数组，
其中两个元素为两个出现了奇数次的元素,请将他们按从小到大排列。

测试样例：
[1,2,4,4,2,1,3,5],8
返回：[3,5]
'''
class OddAppearance:
    def findOdds(self, arr, n):
        # write code here
        xor1 = 0
        for i in arr:
            xor1 ^= i
        a = xor1
        i = -1
        while True:
            b = xor1 & 1
            i += 1
            xor1 >>= 1
            if b == 1:
                break
        xor2 = 0
        for j in arr:
            if (j >> i) & 1 == 1:
                xor2 ^= j
        xor1 = xor2 ^ a
        return [xor1, xor2] if xor1 < xor2 else [xor2, xor1]
