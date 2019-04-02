# -*- coding:utf-8 -*-
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''

# emmmm...maybe time complexity is not correct...
# later, I will check it again.

class Solution:
    def __init__(self):
        self.res = []
    def push(self, node):
        return self.res.append(node)
    def pop(self):
        return self.res.pop()
    def top(self):
        return self.res[-1]
    def min(self):
        return min(self.res)
