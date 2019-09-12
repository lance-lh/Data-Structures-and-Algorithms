'''
输入带有重复值的有序数组，
输出去重后的数组长度
input:
    1,2,2
output:
    2
'''

arr = list(map(int,input().split(',')))
narr = list(set(arr))
print(len(narr))