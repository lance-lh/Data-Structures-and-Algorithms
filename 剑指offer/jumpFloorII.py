# -*- coding:utf-8 -*-
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''


# this question is based on jumpFloor
# and according to the mathematical induction,
# it can be solved by computing the power of given number

def jumpFloorII(number):
    if number < 0:
        return None
    else:
        return power(2,number - 1)

def power(num, i):
    res = 1
    for j in range(i):
        res *= num
    return res

# test
print(jumpFloorII(3))