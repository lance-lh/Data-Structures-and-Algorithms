# -*- coding:utf-8 -*-
'''
对于两个32位整数a和b，请设计一个算法返回a和b中较大的。但是不能用任何比较判断。
若两数相同，返回任意一个。

给定两个整数a和b，请返回较大的数。

测试样例：
1,2
返回：2
'''

class Compare:
    def getMax(self, a, b):
        # write code here
        c = a - b
        sign = (c >> 31) & 1
        flip_sign = sign ^ 1
        return sign * b + flip_sign * a