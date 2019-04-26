# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # return sum([num1, num2])
        while num2:
            num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, ((num1 & num2) << 1) & 0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)

#test
num1 = 9
num2 = -17
print(Solution().Add(num1, num2))