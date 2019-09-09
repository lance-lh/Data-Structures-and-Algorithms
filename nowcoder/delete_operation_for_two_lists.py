'''
输入两个整数数组A和B，A，B仅为数字顺序不同
现在同时在A和B中删除同样数量的数字，使得A和B中剩下的子序列完全相同
求至少从A中删除多少个元素

    input:
        4
        1 3 5 2
        3 2 1 5
    output:
        2
'''

'''
solution 2: 最长递增子序列，O(nlogn)
A和B数字一样，顺序不同
1. 确定B中每个数在A中的索引ind
2. 递增的遍历第二个数组，只要ind是递增的,则对应的递增序列一定是公共序列
（找最长的公共序列，就等价于对第二个数组中的数在第一个数组中索引的最长递增子序列）
'''
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# '''
# do not use list.index() in for-loop, since it costs O(n) time
a_map = [0] * 10000
b_indlist = [0] * n
# fill index of each a element into a_map, the list index is the value of element
for i in range(n):
    a_map[A[i]] = i
for j in range(n):
    b_indlist[j] = a_map[B[j]]
# print(b_indlist)
dp = [10000] * 10000
from bisect import bisect_left
for i in range(n):
    dp[bisect_left(dp,b_indlist[i])] = b_indlist[i]
# print(dp)
print(n-bisect_left(dp,10000))
# '''

'''
Solution 1: 最大公共子序列， O(n^2), TLE
'''
'''
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# create a dp table
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        # update state
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j],dp[i][j]+(A[i] == B[j]))
print(n-dp[-1][-1])
'''
