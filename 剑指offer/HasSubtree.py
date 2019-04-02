# -*- coding:utf-8 -*-

'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        #当pRoot1和pRoot2都不为零的时候，才进行比较。否则直接返回false
        if pRoot1 and pRoot2:
            #如果找到了对应pRoot2的根节点的点
            if pRoot1.val == pRoot2.val:
                #以这个根节点为为起点判断是否包含pRoot2
                res = self.Tree1HasTree2(pRoot1, pRoot2)
            #如果找不到，那么就再去root的左儿子当作起点，去判断时候包含pRoot2
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            #如果还找不到，那么就再去root的右儿子当作起点，去判断时候包含pRoot2
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    # 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    # 如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
    def Tree1HasTree2(self,node1, node2):
        #如果node2已经遍历完了都能对应的上，返回true
        if not node2:
            return True
        #如果node2还没有遍历完，node1却遍历完了。返回false
        if not node1:
            return False
        #如果其中有一个点没有对应上，返回false
        if node1.val != node2.val:
            return False
        #如果根节点对应的上，那么就分别去子节点里面匹配
        return self.Tree1HasTree2(node1.left, node2.left) and self.Tree1HasTree2(node1.right, node2.right)