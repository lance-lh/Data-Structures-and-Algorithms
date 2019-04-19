'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

# 先中序遍历，将所有的节点保存到一个列表中。
# 对这个list[:-1]进行遍历，每个节点的right设为下一个节点，
# 下一个节点的left设为上一个节点。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        self.arr = []
        self.inOrderTraversal(pRootOfTree)
        # since last right pointer points None, so
        # if the length of arr is n, it contains (n - 1) pointers
        for k, v in enumerate(self.arr[:-1]):
            v.right = self.arr[k + 1]
            self.arr[k + 1].left = v
        # return the head node
        return self.arr[0]

    def inOrderTraversal(self, root):
        if not root:
            return None
        self.inOrderTraversal(root.left)
        self.arr.append(root)
        self.inOrderTraversal(root.right)