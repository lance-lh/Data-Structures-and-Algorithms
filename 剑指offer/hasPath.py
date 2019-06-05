# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        '''
        :param matrix: list
        :param rows: int
        :param cols: int
        :param path: str
        :return: bool
        '''

        # check valid or not
        if not matrix or rows < 1 or cols < 1 or not path:
            return False

        # set a same dim visited
        visited = [False] * (rows*cols)

        # set pathind
        pathLen = 0

        # select (0,0) as initial start point
        # check if the matrix has target path
        for r in range(rows):
            for c in range(cols):
                # if current r and c in matrix equal to letter in path
                if self.dfs(matrix,rows,cols,path,visited,r,c,pathLen):
                    return True
        return False

    def dfs(self, matrix, rows, cols, path, visited, r,c,pathLen):
        # end condition
        if pathLen == len(path):
            return True

        # set flag to check string at four directions
        # and in the end, return flag to indicate if current pos includes target char
        flag = False

        # valid check and update pathLen and visited
        # visited should be False
        if r >= 0 and r < rows and c >= 0 and c < cols and \
            matrix[r*cols+c] == path[pathLen] and not visited[r*cols+c]:
            pathLen += 1
            visited[r*cols+c] = True

            flag = self.dfs(matrix,rows,cols,path,visited,r,c-1,pathLen) \
                or self.dfs(matrix,rows,cols,path,visited,r,c+1,pathLen) \
                or self.dfs(matrix,rows,cols,path,visited,r-1,c,pathLen) \
                or self.dfs(matrix,rows,cols,path,visited,r+1,c,pathLen)

            if not flag:
                pathLen -= 1
                visited[r*cols+c] = False
        return flag
