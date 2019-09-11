'''
dota游戏中，n种元素，m个元素可以组成一个新技能
m个元素通过旋转或者反转得到的技能算作重复
例如
    123,231,312,321,213,132
求召唤师可以组合多少种技能?
注：
    20000>=n>=1
    1<=m<=10000
结果对1000000007取余
'''
[n,m] = list(map(int,input().split()))
import itertools
nums = [i for i in range(1,n+1)]
perm = list(itertools.combinations_with_replacement(nums,m))
# print(perm)
print(len(perm)%1000000007)