# -*- coding:utf-8 -*-

'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

def rectCover(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    tmp = [0, 1, 2]

    if number > 2:
        for i in range(3, number + 1):
            tmp.append(tmp[i - 1] + tmp[i - 2])

    return tmp[number]


# test
num = 5
print(rectCover(num))