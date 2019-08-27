'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''
class Solution:
    def solveNQueens(self, n):
        '''
        :param n: int
        :return: List[List[str]
        '''
        def dfs(r):
            # base case
            if r == n:
                res.append([''.join(row) for row in chess])
                return
            # dfs backstracking
            # pass r to dfs, and then decide c in n
            for c in range(n):
                # check previous state
                if isValid(r,c):
                    chess[r][c] = 'Q'
                    # fill row by row
                    dfs(r+1)
                    # if not found exist, run bellow
                    chess[r][c] = '.'
        # condition
        def isValid(r,c):
            # check previous
            # i to current r, j to n
            for i in range(r):
                for j in range(n):
                    if chess[i][j] == 'Q' and (c == j or i+j == r+c or i-j == r-c):
                        return False
            return True

        # global variable res
        res = []
        chess = [['.'] * n for _ in range(n)]
        # start from row 0
        dfs(0)
        return res
#
# if __name__ == 'main':
#     n = 4
#     print(Solution().solveNQueens(n))