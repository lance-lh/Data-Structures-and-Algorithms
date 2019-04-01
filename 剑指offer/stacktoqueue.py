# -*- coding:utf-8 -*-

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

# The idea behind this is very simple. using stack1 (FIFO) to contain all queue data that passes in
# and then pop all stack1 elements to stack2 (FIFO)
# now stack1 and stack2 have opposite order, finally pop the stack2 elements
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if not len(self.stack1) and not len(self.stack2):
            return

        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()