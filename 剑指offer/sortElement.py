# -*- coding:utf-8 -*-
'''
已知一个几乎有序的数组，几乎有序是指，如果把数组排好顺序的话，
每个元素移动的距离可以不超过k，并且k相对于数组来说比较小。
请选择一个合适的排序算法针对这个数据进行排序。

给定一个int数组A，同时给定A的大小n和题意中的k，请返回排序后的数组。

测试样例：
[2,1,4,3,6,5,8,7,10,9],10,2
返回：[1,2,3,4,5,6,7,8,9,10]
'''
class ScaleSort:
    def sortElement(self, A, n, k):
        '''
        :param A: arr
        :param n: len(arr)
        :param k: int
        :return: arr
        '''

        '''
        # write code here
        import heapq
        res = []
        for i in range(0,n-k+1):
            # tmp = A[i:i + k]
            # heapq.heapify(tmp)
            heapq.heapify(A)
            # print(tmp)
            minval = heapq.heappop(A)
            res.append(minval)
            # A[i] = minval
            # print(tmp)
        return res
        '''
        import heapq
        res = []
        while A:
            heapq.heapify(A)
            minval = heapq.heappop(A)
            res.append(minval)
        return res

A = [2,1,4,3,6,5,8,7,10,9]
n = 10
k = 2
print(ScaleSort().sortElement(A,n,k))