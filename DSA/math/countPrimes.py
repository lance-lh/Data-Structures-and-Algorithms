class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n // 2 + 1):
            if res[i] == True:
                res[i * i: n: i] = [False] * len(res[i * i: n: i])
        return sum(res)
# test
n = 10
print(Solution().countPrimes(n))