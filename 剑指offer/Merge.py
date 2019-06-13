# -*- coding:utf-8 -*-

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative solution
'''
class Solution:
    # 返回合并后列表
    def Merge(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2

        head = cur = ListNode(0)

        while head1 and head2:
            if head1.val > head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next
            cur = cur.next
        cur.next = head1 or head2
        return head.next
'''

# recursive solution
class Solution:
    # 返回合并后列表
    def Merge(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2
        head = ListNode(0)

        if head1.val < head2.val:
            head = head1
            head.next = self.Merge(head1.next, head2)
        else:
            head = head2
            head2.next = self.Merge(head1, head2.next)
        return head