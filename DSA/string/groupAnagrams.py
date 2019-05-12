class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)

        for i in strs:
            d[tuple(sorted(i))].append(i)
        return d.values()


# test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))