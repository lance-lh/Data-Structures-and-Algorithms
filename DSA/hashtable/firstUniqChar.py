class Solution:
    def firstUniqChar(self, s):
        '''
        :param s: str
        :return: int
        '''
        from collections import OrderedDict
        d = OrderedDict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in d:
            if d[j] == 1:
                return s.index(j)
        return -1



# test
s = 'loveleetcode'
print(Solution().firstUniqChar(s))