# -*- coding:utf-8 -*-

'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''


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
        # res to hold result
        # cur to hold current layer node addr
        # tmp to hold temp value
        # new to hold temp node addr
        res, cur = [], [root]
        while cur:
            tmp, new = [],[]
            for node in cur:
                tmp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            #res.append(tmp)  while this is correct in leetcode
            # leetcode: python 3
            # nowcoder: python 2.7
            res += tmp
            cur = new
        return res