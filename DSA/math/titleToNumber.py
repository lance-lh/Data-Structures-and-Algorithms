class Solution:
    def titleToNumber(self, s: str) -> int:
        from functools import reduce
        return reduce(lambda x,y: x*26+y, [ord(c)-ord('A')+1 for c in s])

# test
alpha = 'ZY'
print(Solution().titleToNumber(alpha))