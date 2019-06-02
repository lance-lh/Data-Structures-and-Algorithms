# -*- coding:utf-8 -*-

'''
一个整型数组里除了一个数字之外，其他的数字都出现了三次。请写程序找出这一个只出现一次的数字。
'''


# bit manipulation
class Solution:
    def FindNumsAppearOnce(self, array):
        # assuming 32 bit
        bitSum = [0] * 32
        # i denotes num in array
        for i in range(len(array)):
            bitMask = 1
            # j 按照从右往左顺序(即从低位到高位的顺序)
            for j in range(31,-1,-1):
                bit = array[i] & bitMask
                if bit != 0:
                    bitSum[j] += 1
                bitMask <<= 1
        res = 0
        for i in range(0,32):
            # 左移表示新数
            res <<= 1
            res += bitSum[i] % 3
        return res

# bitSum: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6, 7]
# i = 29, res = 1
# i = 30, res = 1*2+0
# i = 31, res = 1*2*2+1=5

# test
nums = [7,1,6,6,1,4,5,1,6,4,7,4,7]
print(Solution().FindNumsAppearOnce(nums))