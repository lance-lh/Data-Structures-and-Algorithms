# -*- coding:utf-8 -*-

'''
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False

        stack = []
        for i in pushV:
            # 按照pushV的顺序将元素添加到列表中
            stack.append(i)
            # stack不为空，并且stack中最后元素等于弹出列表的第一个元素
            # 元素不相等就一直添加，直到满足相等关系则弹出
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        # 最后stack中应该为空，否则表示不对应上popV中元素
        if len(stack):
            return False
        else:
            return True