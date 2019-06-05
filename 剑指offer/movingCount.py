# -*- coding:utf-8 -*-

# backtracking
class Solution:
    def movingCount(self, threshold, rows, cols):
        '''
        :param threshold: List[int]
        :param rows: int
        :param cols: int
        :return: int
        '''

        # check boundary
        if threshold < 0 or rows < 1 or cols < 1:
            return 0

        # set visited
        visited = [False] * (rows * cols)

        # dfs
        count = self.dfs(threshold,rows,cols,0,0,visited)

        return count

    def dfs(self,threshold,rows,cols,r,c,visited):
        cnt = 0
        # check whether it can reach (r,c)
        if self.check(threshold,rows,cols,r,c,visited):
            visited[r*cols+c] = True

            cnt = 1 + self.dfs(threshold,rows,cols,r,c+1,visited) \
                      + self.dfs(threshold,rows,cols,r,c-1,visited) \
                      + self.dfs(threshold,rows,cols,r+1,c,visited) \
                      + self.dfs(threshold,rows,cols,r-1,c,visited)
        return cnt

    def check(self,threshold,rows,cols,r,c,visited):
        if r >= 0 and r < rows and c >= 0 and c < cols \
           and self.getDigitSum(r) + self.getDigitSum(c) <= threshold \
           and not visited[r*cols+c]:
            return True
        return False

    def getDigitSum(self,num):
        numSum = 0
        while num > 0:
            numSum += num % 10
            num /= 10
        return numSum