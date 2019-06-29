#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between). 
#
# 
#For example: 
#Given binary tree [3,9,20,null,null,15,7], 
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 
# 
# 
#return its zigzag level order traversal as: 
# 
#[
#  [3],
#  [20,9],
#  [15,7]
#]
# 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, cur = [], [root]
        level = 0
        while cur:
            curval, nextrow = [], []
            for node in cur:
                curval.append(node.val)
                if node.left:
                    nextrow.append(node.left)
                if node.right:
                    nextrow.append(node.right)
            if level % 2 == 1:
                curval = curval[::-1]

            res.append(curval)
            cur = nextrow
            level += 1
        return res