# -*- coding:utf-8 -*-
'''
输入一颗二叉树的跟节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    '''
    当前节点为叶子节点并和整数值相等时直接输出，
    当前节点值大于整数值输出空，当前节点值小于整数值，
    则更新整数值递归下去寻找路径，注意根节点与递归得到的路径如何合并，
    '''
    def FindPath(self, root, expectNumber):
        #空树或根节点值大的情况直接返回
        if not root or root.val > expectNumber:
            return []
        #叶子节点情况, not root.left and not root.right
        #注意需返回二维list
        #利用ｒoot遍历，expectNumber会每次减去加进去的长度
        #只有满足遍历到叶节点，以及路径和相等才说明找到一条路径
        #基
        if not root.left and not root.right and root.val==expectNumber:
            return [[root.val]]
        else:
            expectNumber -= root.val
            #递归分别求左右子树中的路径
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)
            #与根节点合并
            result = [[root.val]+x for x in left]
            for x in right:
                result.append([root.val]+x)
            #输出按路径长度排序的路径列表
        return sorted(result, key=lambda x:-len(x))