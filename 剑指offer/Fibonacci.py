# -*- coding:utf-8 -*-
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''

# method 1: recursive
# def Fibonacci(n):
#     n must be int type
#     if not isinstance(n, int):
#         return None
#     # check special case 0
#     if n == 0:
#         return 0
#     # check special case 1
#     if n == 1:
#         return 1
#
#     if n >= 2:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)


def Fibonacci(n):
    # n must be int type
    if not isinstance(n, int):
        return None
    # check special case 0
    if n == 0:
        return 0
    # check special case 1
    if n == 1:
        return 1
    tmp = [0, 1]

    if n >= 2:
        # range: 2, 3, 4, ... , n
        for i in range(2, n + 1):
            tmp.append(tmp[i - 2] + tmp[i - 1])
    # return value is location n, not n-th value
    return tmp[n]


# test
n = 6
print(Fibonacci(n))