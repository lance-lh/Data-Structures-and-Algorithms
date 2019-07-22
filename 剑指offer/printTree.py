# -*- coding:utf-8 -*-
'''
有一棵二叉树，请设计一个算法，按照层次打印这棵二叉树。

给定二叉树的根结点root，请返回打印结果，结果按照每一层一个数组进行储存，
所有数组的顺序按照层数从上往下，且每一层的数组内元素按照从左往右排列。保证结点数小于等于500。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreePrinter:
    def printTree(self, root):
        # write code here
        if not root:
            return
        res, cur = [],[root]
        while cur:
            temp, nextrow = [],[]
            for node in cur:
                temp.append(node.val)
                if node.left:
                    nextrow.append(node.left)
                if node.right:
                    nextrow.append(node.right)
            cur = nextrow
            res.append(temp)
        return res