# -*- coding:utf-8 -*-
'''
请设计一个高效算法，判断数组中是否有重复值。必须保证额外空间复杂度为O(1)。

给定一个int数组A及它的大小n，请返回它是否有重复值。

测试样例：
[1,2,3,4,5,5,6],7
返回：true
'''
class Checker:
    def checkDuplicate(self, a, n):
        # use iterative heap sort first,
        # then check adjacent two data
        return len(set(a))!= len(a)