'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
'''

'''
class Solution:
    def totalNQueens(self, n):

        # :param n: int
        # :return: int

        res = []
        self.dfs([-1] * n, 0, [], res)
        return len(res)

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.Isvalid(nums, index):
                tmp = '.' * len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + 'Q' + tmp[i + 1:]], res)

    def Isvalid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True
'''
# use global self.res to record result
# remove res and path from dfs paras
class Solution:
    def totalNQueens(self, n):
        '''
        :param n: int
        :return: int
        '''
        self.res = 0
        self.dfs([-1]*n,0)
        return self.res
    def dfs(self,nums,index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.Isvalid(nums,index):
                self.dfs(nums,index+1)

    def Isvalid(self,nums,n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

# test
if __name__ == 'main':
    n = 4
    print(Solution().totalNQueens(n))