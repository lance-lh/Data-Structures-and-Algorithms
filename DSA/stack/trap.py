'''
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

# 单调栈应用（单减栈）
# 接雨水需要满足一个U形，维护一个单减栈，纪录index
class Solution:
    def trap(self, height):
        '''
        :param height: List[int]
        :return: int
        '''
        res = 0
        # stack to store index
        stack = []
        i = 0
        # for-loop is not ok
        # for i in range(len(height)):
        while i < len(height):
            #
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            # if height[i] > stack[-1]
            # 当读取到高度值大于栈顶index对应height,说明当前位置满足U形，可以计算面积
            else:
                # 取出U形谷底，弹出
                valley = stack[-1]
                stack.pop()
                # 弹出后如果stack中为空，跳转到下次判断
                if not stack:
                    continue
                # width calculation
                w = i - stack[-1] - 1
                # height calculation
                h = min(height[stack[-1]],height[i]) - height[valley]
                res += w * h
        return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))