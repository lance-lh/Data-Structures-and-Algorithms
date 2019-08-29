n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

create a dp table
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        # update state
        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j],dp[i][j]+(A[i] == B[j]))
print(n-dp[-1][-1])
'''
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    dp[i][-1] = n - i

for j in range(n):
    dp[-1][j] = n - j

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if A[i] == B[j]:
            dp[i][j] = dp[i+1][j+1]
        else:
            dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1])
print(dp[0][0]//2)
'''


memo = {}
def dp(i,j):
    if (i,j) not in memo:
        if i == n or j == n:
            res = 2*n - i -j
        elif A[i] == B[j]:
            res = dp(i+1,j+1)
        else:
            res = 1+min(dp(i+1,j),dp(i,j+1))
        memo[i,j] = res
    return memo[i,j]
print(dp(0,0)//2)

'''
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1, n + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(n-dp[-1][-1])
'''
# 4
# 1 3 5 2
# 3 2 1 5


