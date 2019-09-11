#!/bin/python
# -*- coding: utf8 -*-
'''
输入两个整数序列A和B，输出同时在A，B中出现的最长子序列的长度
注意：子序列由原序列中的连续元素组成

(实质上为最长公共子串问题[连续])
input:
    5
    1 2 3 2 1
    5
    3 2 1 4 7

output:
    3

explain:
    最长重复子列为[3,2,1]
'''
# ******************************开始写代码******************************
def findMaxSubListLen(a, b):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = 0
    res = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] >= res:
                res = dp[i][j]
    return res


# ******************************结束写代码******************************
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

res = findMaxSubListLen(a, b)

print(str(res) + "\n")