# -*- coding:utf-8 -*-
'''
有两个从小到大排序以后的数组A和B，其中A的末端有足够的缓冲空容纳B。
请编写一个方法，将B合并入A并排序。

给定两个有序int数组A和B，A中的缓冲空用0填充，
同时给定A和B的真实大小int n和int m，请返回合并后的数组。
'''
class Merge:
    def mergeAB(self, A, B, n, m):
        # write code here
        k = n + m - 1
        i,j = n-1,m-1
        while i >= 0 and j >= 0:
            if A[i] <= B[j]:
                A[k] = B[j]
                k -= 1
                j -= 1
            else:
                A[k] = A[i]
                k -= 1
                i -= 1
        while i >= 0:
            A[k] = A[i]
            k -= 1
            i -= 1
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1
        return A