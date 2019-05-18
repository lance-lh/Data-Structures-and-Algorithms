class Solution:
    def findAnagrams(self, s, p):
        '''
        :param s: str
        :param p: str
        :return: List[int]
        '''
        from collections import Counter
        ls, lp = len(s), len(p)
        cp = Counter(p)
        cs = Counter()
        res = []
        for i in range(ls):
            cs[s[i]] += 1
            if i >= lp:
                # when add a new element
                # in cs, the leftmost key value minus 1
                cs[s[i - lp]] -= 1
                # delete the leftmost key
                if cs[s[i - lp]] == 0:
                    del cs[s[i - lp]]
            if cs == cp:
                res.append(i - lp + 1)
        return res

# test
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s,p))