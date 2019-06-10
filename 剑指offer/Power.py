# -*- coding:utf-8 -*-

'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

'''
def Power(base, exponent):
    if base == 0:
        return 0
    res = 1
    if exponent > 0:
        for i in range(exponent):
            res *= base
        return res
    else:
        for j in range(abs(exponent)):
            res *= base
        return 1 / res
'''


class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        res = 1
        b = base
        e = abs(exponent)
        while e > 0:
            if e & 1:
                res *= b
            # e // 2 to find 1 from low pos to high pos
            e >>= 1
            # power(b,subexponent)
            b *= b
        return res if exponent >= 0 else 1/res