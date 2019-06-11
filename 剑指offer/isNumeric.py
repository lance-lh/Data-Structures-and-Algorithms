# -*- coding:utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''


# 内置float函数
'''
class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            ss = float(s)
            return True
        except:
            return False
'''

# 正则化
'''
import re
'''

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        hasE = False
        hassign = False
        haspoint = False
        if not s:
            return False
        for i in range(len(s)):
            if s[i] == "e" or s[i] == "E":
                # e后面一定要有数字
                if i==len(s)-1:
                    return False
                # 只有１个e
                if hasE:
                    return False
                hasE = True
            elif s[i]=="+" or s[i]=="-":
                # 第二次出现符号要紧跟e后面
                if hassign and s[i-1] != "e" and s[i-1] != "E":
                    return False
                # 第一次出现符号，且不在开头，那么也要紧跟e后面
                if not hassign and i>0 and s[i-1] != "e" and s[i-1] != "E":
                    return False
                hassign = True
            elif s[i]==".":
                # 小数点不在e后面且不能出现两次
                if hasE or haspoint:
                    return False
                haspoint = True
            elif s[i]<"0" or s[i]>"9":
                return False
        return True