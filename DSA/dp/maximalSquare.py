class Solution:
    def maximalSquare(self, matrix):
        '''
        :param matrix: List[List[str]]
        :return: int
        '''
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     dp[i][0] = matrix[i][0]
        # for j in range(n):
        #     dp[0][j] = matrix[0][j]

        # in case only 1
        res = max(max(dp))
        for i in range(1, m):
            for j in range(1, n):
                # if matrix[i][j] == '1':
                dp[i][j] = (min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1) * int(matrix[i][j])
                # else:
                # dp[i][j] = 0
                res = max(res, dp[i][j])
        return res ** 2


# test
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(matrix))