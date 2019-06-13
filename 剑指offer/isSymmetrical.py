# -*- coding:utf-8 -*-

'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetrical(self, root):
        if not root:
            return True
        return self.isSymmetricalTree(root.left,root.right)

    def isSymmetricalTree(self,left,right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.isSymmetricalTree(left.left,right.right) and self.isSymmetricalTree(left.right,right.left)