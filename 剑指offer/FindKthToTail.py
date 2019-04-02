# -*- coding:utf-8 -*-
'''
输入一个链表，输出该链表中倒数第k个结点。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if k > len(stack) or k < 1:
            return
        return stack.pop(-k)