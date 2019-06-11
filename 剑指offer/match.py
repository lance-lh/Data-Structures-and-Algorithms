# -*- coding:utf-8 -*-

# recursion
'''
class Solution:
    # s, pattern都是字符串
    def match(self, s, p):
        if not p:
            return not s

        first_try = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_try and self.isMatch(s[1:], p)
        else:
            return first_try and self.isMatch(s[1:], p[1:])
'''

# dp, bottom to up
class Solution:
    # s, pattern都是字符串
    def match(self, s, p):
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s),-1,-1):
            for j in range(len(p)-1,-1,-1):
                first_try = i < len(s) and p[j] in {s[i],'.'}
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_try and dp[i+1][j]
                else:
                    dp[i][j] = first_try and dp[i+1][j+1]
        return dp[0][0]