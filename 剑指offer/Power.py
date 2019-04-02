# -*- coding:utf-8 -*-

'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

def Power(base, exponent):
    if not isinstance(base, float) and not isinstance(exponent, int):
        return None
    res = 1
    if exponent > 0:
        for i in range(exponent):
            res *= base
        return res
    else:
        for j in range(abs(exponent)):
            res *= base
        return 1 / res
