# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# method 1: using min()
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         if not rotateArray:
#             return 0
#         else:
#             return min(rotateArray)

# method 2: using list.sort()
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         if not rotateArray:
#             return 0
#         else:
#             rotateArray.sort()
#             return rotateArray[0]

# method 3: binary search
# 链接：https://www.nowcoder.com/questionTerminal/9f3231a991af4f55b95579b44b7a01ba
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 思路应该是二分查找
        # 下面使用 递归实现2分查找，其中递归的时候必须使用return！！！ 不然会返回none
        start = 0
        end = len(rotateArray) - 1
        mid = int((start + end) / 2)
        if len(rotateArray) == 2:
            if rotateArray[0] > rotateArray[1]:
                return rotateArray[1]
            else:
                return rotateArray[0]

        elif rotateArray[mid] > rotateArray[end]:
            return self.minNumberInRotateArray(rotateArray[mid:end + 1])
        elif rotateArray[mid] < rotateArray[start]:
            return self.minNumberInRotateArray(rotateArray[start:mid + 1])
'''       
        


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return

        start = 0
        end = len(rotateArray)-1
        mid = start

        # rotate 0 data, which means the list is already sorted!
        # if rotateArray[start] < rotateArray[end]:
        #     return rotateArray[start]
        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                mid = end
                break

            mid = (start + end) // 2

            # if start, end and mid ptr points to the equal number in array
            # then we should search from left to right
            if rotateArray[start] == rotateArray[mid] and rotateArray[end] == rotateArray[mid]:
                return self.Inorder(rotateArray, start, end)

            # since rotatearray, if mid in left part, i.e.,mid > start, update start
            # if mid in the right part, mid < end, update end
            if rotateArray[mid] >= rotateArray[start]:
                start = mid
            elif rotateArray[mid] <= rotateArray[end]:
                end = mid

        return rotateArray[mid]

    def Inorder(self, rotateArray,start,end):
        res = rotateArray[start]
        for i in range(start+1, end+1):
            if rotateArray[i] < res:
                res = rotateArray[i]
        return result