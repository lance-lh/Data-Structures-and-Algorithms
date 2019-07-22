# -*- coding:utf-8 -*-
'''
有一个整型数组A，其中只有一个数出现了奇数次，其他的数都出现了偶数次，
请打印这个数。要求时间复杂度为O(N)，额外空间复杂度为O(1)。

给定整形数组A及它的大小n，请返回题目所求数字。

测试样例：
[1,2,3,2,1],5
返回：3
'''

class OddAppearance:
    def findOdd(self, A, n):
        # write code here
        xor = 0
        for i in A:
            xor ^= i
        return xor