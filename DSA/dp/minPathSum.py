'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution:
    def minPathSum(self, grid):
        '''
        :param grid: List[List[int]]
        :return: int
        '''
        # the minimum path sum of arriving at pos (i,j)
        m,n = len(grid),len(grid[0])
        for i in range(1,m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1,n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = min(grid[i][j-1],grid[i-1][j])+grid[i][j]
        return grid[-1][-1]

# test
grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]
print(Solution().minPathSum(grid))