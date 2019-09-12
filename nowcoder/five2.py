'''
leetcode: 135 Candy
input:
    6
    3
    6
    3
    5
    6
    2
output:
    10
explanation:
    first line represents nums of input
    input: [6 3 6 5 6 2]
    means: [1 2 1 2 3 1]
    sum(means): 10
'''

n = int(input())
stu = []
for i in range(n):
    stu.append(int(input()))
# print(stu)

res = [1]*n
l,r = 1,1
for i in range(1,n):
    l = l+1 if stu[i] > stu[i-1] else 1
    res[i] = l
for j in range(n-2,-1,-1):
    r = r+1 if stu[j] > stu[j+1] else 1
    res[j] = max(r,res[j])
print(sum(res))

'''
dp = [1] * n
i,j = 0,1
while j <n:
    if stu[i] >= stu[j]:
        dp[j] -= 1
    else:
        dp[j] += 1
    i+=1
    j+=1
minval = min(dp)
addsome = 0
if minval <= 0:
    addsome = -minval +1
if minval > 1:
    addsome = minval -1

if minval <= 0:
    for i in range(n):
        dp[i] += addsome
if minval > 0:
    for j in range(n):
        dp[i] -= addsome
# print(dp)
print(sum(dp))
'''