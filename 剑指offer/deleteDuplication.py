# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative solution, add new node before pHead
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        new = ListNode(-1)
        new.next = pHead
        pre = new
        p = pHead
        # we don't know q is None or not
        q = None
        while p and p.next:
            q = p.next
            if p.val == q.val:
                # q移动到接下来第一个不等于ｐ的位置
                while q and p.val == q.val:
                    q = q.next
                # 删除中间的所有重复节点
                pre.next = q
                p = q
            else:
                pre = p
                p = p.next
        return new.next