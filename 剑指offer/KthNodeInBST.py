# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot:
            return

        order = self.InOrderTraversal(pRoot)
        if len(order) < k or k == 0:
            return
        return order[k - 1]

    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            # note: here is root, not root.val
            res.append(root)
            res += self.InOrderTraversal(root.right)
        return res