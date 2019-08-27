'''
一行代码转置矩阵
'''
a = [[1,2],[3,4]]
b = list(map(list,zip(*a)))
print(b)