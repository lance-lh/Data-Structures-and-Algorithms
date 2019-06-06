# -*- coding:utf-8 -*-

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

'''
def NumberOf1(n):
    if not isinstance(n,int):
        return None

    cnt = 0
    if n < 0:
        # 对于负数，最高位为1，而负数在计算机是以补码存在的，往右移，符号位不变，
        # 符号位1往右移，最终可能会出现全1的情况，导致死循环。与0xffffffff相与，就可以消除负数的影响
        # 相当于求补码
        n = n & 0xffffffff
    while n:
        # n != 0 it must have 1.
        cnt += 1
        n = (n - 1) & n
    return cnt
'''

'''
def NumberOf1(n):
    if not isinstance(n,int):
        return None
    if n >= 0:
        return bin(n).count('1')
    else:
        # convert negative to its complemented version
        return bin(2**32 + n).count('1')
'''
def NumberOf1(n):
    cnt = 0
    # limit 32 bits
    n = n & 0xffffffff
    while n:
        cnt += 1
        n &= n - 1
    return cnt


# test
num = -7
print(NumberOf1(num))