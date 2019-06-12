# -*- coding:utf-8 -*-

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
# time: O(n)
# space: O(n)
def reOrderArray(array):
    if not array:
        return []

    odd_lst = []
    even_lst = []

    for i in array:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    return odd_lst + even_lst
'''

# time: O(n^2)
# space: O(1)
class Solution:
    def reOrderArray(self, array):
        if not array:
            return []
        for i in range(len(array)):
            cur = array[i]
            # if cur is 奇数
            if not self.isEven(array[i]):
                pre = i - 1
                # 找pre和pre之前的偶数
                while pre >= 0 and self.isEven(array[pre]):
                    array[pre+1] = array[pre]
                    pre -= 1
                array[pre+1] = cur
        return array

    def isEven(self,n):
        return n & 1 == 0





# test
array = [1, 4, 6, 3, 5, 8, 4,7]
print(Solution().reOrderArray(array))