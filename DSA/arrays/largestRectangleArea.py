class Solution:
    def largestRectangleArea(self, heights):
        '''
        :param heights: : List[int]
        :return: int
        '''
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res


# test
heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))