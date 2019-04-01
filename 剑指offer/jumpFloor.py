# -*- coding:utf-8 -*-
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

# according to mathematical induction, this is a Fibonacci problem.
# we can utilize recursive and iterative solutions to solve it.

# recursive solution, but waste time
# def jumpFloor(number):
#     if number <= 0:
#         return None
#     if number == 1:
#         return 1
#     if number == 2:
#         return 2
#     return jumpFloor(number - 1) + jumpFloor(number - 2)

# iterative solution
def jumpFloor(number):
    if number <= 0:
        return None
    if number == 1:
        return 1
    if number == 2:
        return 2
    tmp = [0, 1, 2]
    if number > 2:
        for i in range(3,number+1):
            tmp.append(tmp[i - 1] + tmp[i - 2])
    return tmp[number]

# test
num = 5
print(jumpFloor(num))