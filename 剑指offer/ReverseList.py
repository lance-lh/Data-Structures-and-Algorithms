# -*- coding:utf-8 -*-

'''
输入一个链表，反转链表后，输出新链表的表头。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# stack-based solution
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # if node is empty
        if not pHead:
            return
        # using stack to achieve this
        stack = []
        # traverse the linked list
        while pHead:
            stack.append(pHead)
            pHead = pHead.next
        # stack is not a real stack, we need to reverse it
        stack.reverse()
        # pointers need to be adjusted
        for i in range(0, len(stack)):
            node1 = stack[i]
            if i == len(stack) - 1:
                node1.next = None
            else:
                node2 = stack[i + 1]
                node1.next = node2
        # after reversing and adjusting the pointer, stack[0] is the head node.
        return stack[0]
'''

# recursive solution
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        if not head or not head.next:
            return head
        reversedlist = self.ReverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedlist
'''

# iterative solution
class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        if not head or not head.next:
            return head
        p,q = head,head.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p