'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right

Example 2:
    Input: m = 7, n = 3
    Output: 28
'''
# here, m is column and n is row
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp represents when u arrive at (i,j) pos, how many ways need
        # all pos is initialized with 1
        # start from (1,1)
        dp = [[1 for _ in range(m)] for _ in range(n)]
        # row n
        for i in range(1,n):
            # column m
            for j in range(1,m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

# test
m = 7
n = 3
# m = 3
# n = 2
print(Solution().uniquePaths(m, n))