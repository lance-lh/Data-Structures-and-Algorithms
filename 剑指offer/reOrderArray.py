# -*- coding:utf-8 -*-

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

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

# test
array = [1, 4, 6, 3, 5, 8, 4,7]
print(reOrderArray(array))