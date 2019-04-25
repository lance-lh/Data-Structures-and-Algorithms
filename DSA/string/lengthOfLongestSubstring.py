# Brute-Force solution
# time complexity: O(n^3)
# Time Limit Exceeded
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        :param s: str
        :return: int
        '''
        res = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.checkduplicate(s,i,j):
                    res = max(res,j - i)
        return res

    def checkduplicate(self, s, start, end):
        lst = ""
        for i in range(start, end):
            ch = s[i]
            if ch in lst:
                return False
            lst += ch
        return True
"""

# sliding window
# time complexity: O(n) but 2n steps
# AC
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        :param s: str
        :return: int
        '''
        res, i, j = 0,0,0
        lst = []

        while i < len(s) and j < len(s):
            if s[j] not in lst:
                lst.append(s[j])
                j += 1
                res = max(res, j - i)
            else:
                lst.remove(s[i])
                i += 1
        return res
"""

# sliding window optimized
# time complexity: O(n) but n steps
# AC
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        :param s: str
        :return: int
        '''

        d = {}
        res = 0
        start = 0
        for i,ch in enumerate(s):
            if ch in d:
                start = max(start, d[ch] + 1)
            # i and start are 0-indexed varibles
            res = max(res, i - start + 1)
            d[ch] = i
        return res


# test
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))