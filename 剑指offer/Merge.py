# -*- coding:utf-8 -*-

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # create a new empty node as head
        dummy = ListNode(0)
        # fetch the new head addr to pHead
        pHead = dummy

        # traverse till one list to the last node
        # use dummy to lead the pHead2 or pHead1
        # finally, dummy becomes the last node of the list
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next

            dummy = dummy.next

        # pHead1.val >= pHead2.val
        if pHead1:
            dummy.next = pHead1
        # pHead1.val < pHead2.val
        elif pHead2:
            dummy.next = pHead2
        return pHead.next
