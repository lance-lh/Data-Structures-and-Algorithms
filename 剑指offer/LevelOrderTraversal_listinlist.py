# -*- coding:utf-8 -*-

'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
rtype: List[List]
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res, cur = [], [root]
        while cur:
            curval, nextrow = [], []
            for node in cur:
                curval.append(node.val)
                if node.left:
                    nextrow.append(node.left)
                if node.right:
                    nextrow.append(node.right)
            # return datatype is list
            res.append(curval)
            cur = nextrow
        return res