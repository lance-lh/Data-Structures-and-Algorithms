# -*- coding:utf-8 -*-
'''
输入一个链表，输出该链表中倒数第k个结点。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution:
    def FindKthToTail(self, head, k):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if k > len(stack) or k < 1:
            return
        return stack.pop(-k)
'''

class Solution:
    def FindKthToTail(self, head, k):
        #注意三点
        # 1. linked list为空；
        # 2. linked list长度小于ｋ
        # 3. k == 0
        if not head or k == 0:
            return
        ahead = behind = head
        cnt = 0
        # ahead和behind之间相隔了k-1的距离
        for i in range(k-1):
            if ahead.next:
                ahead = ahead.next
            else:
                return
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        return behind