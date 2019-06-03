'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# construct stack and use slice to return result
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        stack = []

        # notice that: if is not a loop, use while instead!
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]


# construct stack and use pop method to return result
'''
# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(self, listNode):
    res, stack = [], []
    
    # notice that: if is not a loop, use while instead!
    while listNode:
        stack.append(listNode.val)
        listNode = listNode.next
        
    while stack:
        res.append(stack.pop())
    return res
'''

# recursive solution
def printListFromTailToHead(self, listNode):
    if not listNode:
        return []
    while listNode:
        return self.printListFromTailToHead(listNode.next) + [listNode.val]