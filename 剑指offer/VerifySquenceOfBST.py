# -*- coding:utf-8 -*-

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # order : left, right, root
        # check
        if not sequence:
            return False
        # BST postorder, the last element is root node
        root = sequence[-1]

        # in BST, left node smaller than root node
        i = 0
        # sequence[:-1] indicates sequence except the last element
        for node in sequence[:-1]:
            if node > root:
                break
            # in description, there are no two same number
            # if node < root, count the left node index i
            i += 1

        # in BST, right node larger than root node
        for node in sequence[i:-1]:
            if node < root:
                return False

        # check wether the left part is BST
        left = True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])

        # # check wether the right part is BST
        right = True
        # i < len(sequence) - 2
        # -1 means the max index of the sequence
        # -2 means that exclude the root node

        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i + 1:-1])

        return left and right