# -*- coding:utf-8 -*-
'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, head):
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # 如果后续为空，则表明无环
        if not fast or not fast.next:
            return

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow