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
        res = []
        self.dfs([-1]*n,0,[],res)
        return res

    def dfs(self,nums, index, path, res):
        '''
        :param nums: 1 d array, e.g.[1,3,0,2], 2nd queen can be placed in column 3
        :param index: index-th queen
        :param path: record already-made decision
        :param res: record global result
        '''
        # define exist when check the last queen, quit
        if index == len(nums):
            res.append(path)
            return  # back tracking
        # for loop to check all possible column index-th queen can be placed
        for i in range(len(nums)):
            # assign i to the place of index-th queen
            nums[index] = i
            if self.Isvalid(nums,index):
                tmp = '.'*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+'Q'+tmp[i+1:]], res)

    # check whether n-th queen can be placed that place
    def Isvalid(self,nums,n):
        # check 0 - n queens pos (state)
        for i in range(n):
            # abs(nums[i] - nums[n]) == n - i to check if the distance of two queens are equal (diagonal )
            # nums[n] == nums[i] to check if two queens are in same column
            if abs(nums[i] - nums[n]) == n - i or nums[n] == nums[i]:
                return False
        return True


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
    '''
#
# if __name__ == 'main':
#     n = 4
#     print(Solution().solveNQueens(n))