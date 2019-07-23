# -*- coding:utf-8 -*-
'''
对于一个数组，请设计一个高效算法计算需要排序的最短子数组的长度。

给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的长度。
(原序列位置从0开始标号,若原序列有序，返回0)。保证A中元素均为正整数。

测试样例：
[1,4,6,5,9,10],6
返回：2
'''
class Subsequence:
    def shortestSubsequence(self, A, n):
        # write code here
        '''
        # left -> right
        largest = 0
        for i in range(n):
            if A[largest] <= A[i] and A[i] > A[i + 1]:
                largest = i
                break
        # rightmost = largest
        for rightmost in range(largest,n):
            if A[largest] < A[rightmost]:
                break
        rightmost -= 1

        smallest = n-1
        for i in range(n-1, -1, -1):
            if A[smallest] >= A[i] and A[i] < A[i - 1]:
                smallest = i
                break
        for leftmost in range(smallest,-1,-1):
            if A[smallest] > A[leftmost]:
                break
        leftmost += 1

        return rightmost - leftmost + 1
        '''

        left, right = 0,0
        # left to right to find max
        maxval = A[0]
        # right to left to find min
        minval = A[n-1]

        for i in range(1,n):
            if A[i] >= maxval:
                maxval = A[i]
            else:
                right = i
        for j in range(n-2,-1,-1):
            if A[j] <= minval:
                minval = A[j]
            else:
                left = j
        if left == 0 and right == 0:
            return 0
        else:
            return right - left + 1

A = [1,4,6,5,9,10]
# A = [1,2,3,3,8,9]
n = 6
print(Subsequence().shortestSubsequence(A,n))