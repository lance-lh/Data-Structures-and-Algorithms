'''
leetcode 64. Minimum Path Sum
从左上角出发，到矩阵右下角，返回所有路径中的最小和
Input:
    3
    3
    1 3 1
    1 5 1
    4 2 1
Output: 7
'''
m = int(input())
n = int(input())
matrix = []
for i in range(m):
    matrix.append(list(map(int,input().split())))

# print(matrix)

for i in range(1,n):
    matrix[0][i] += matrix[0][i-1]
for j in range(1,m):
    matrix[j][0] += matrix[j-1][0]
for i in range(1,m):
    for j in range(1,n):
        matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1])
print(matrix[-1][-1])