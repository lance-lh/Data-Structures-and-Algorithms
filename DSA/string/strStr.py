class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not s or not p:
            return 0
        m, n = len(s), len(p)
        lps = [0] * n
        self.findlps(p, lps, n)

        i, j = 0, 0
        while i < m and j < n:
            if s[i] == p[j]:
                i, j = i + 1, j + 1
            else:
                j = lps[j]
        if j == n:
            return i - j
        return -1

    def findlps(self, p, lps, n):
        i = 1
        # lps[0] is always zero!
        while i < n:
            if p[i]



        # test
s = "mississippi"
p = "issip"
print(Solution().strStr(s, p))