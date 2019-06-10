# -*- coding:utf-8 -*-
class Solution:
    # 判断是否达到了最大的n位数
    def Increment(self,number):
        overFlow=carry=0
        length=len(number)
        # 逆序，从数组高index，即是数字低位开始
        for i in range(length-1,-1,-1):
            # ord()将字符串转换为十进制整数
            # num表示每一位上的数，初始最低位进位为０，以后每一位都会加上carry
            # num=ord(number[i])-ord('0')+carry
            num = int(number[i]) + carry
            # 最低位加１，其他位加carry进位
            if i == length-1:
                num+=1
            if num >= 10:
                if i == 0:
                    overFlow = 1
                else:
                    num-=10
                    carry=1
            else:
                carry=0
            # chr()将整数转化为字符串
            number[i]=str(num)
        return overFlow

    # 打印用字符串表示的数字
    # 找到字符串中最左边的１，打印之后（含）的数，break跳出循环
    def PrintNum(self,number):
        # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
         string=''.join(number)
         for i in range(len(string)):
             if string[i]!='0':
                 print(string[i:])
                 break

    def print1ToMaxNDigits(self,n):
         if n<=0:
             raise Exception('Input Error:n!')
         # n可能为很大的数，需要用数组来模拟，最后再使用join方法
         # 生成一个元素为字符串‘0’的n维数组
         number=['0']*n
         # overflow为０时打印
         while not self.Increment(number):
             self.PrintNum(number)

Solution().print1ToMaxNDigits(3)



'''
# first attempt
def Print1(n):
    if n <= 0:
        return 0
    list_num = []
    for i in range(1,10**n):
        list_num.append(i)
    return list_num

# test
n = 2
print(Print1(n))
'''