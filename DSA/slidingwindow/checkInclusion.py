class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """


        if len(s1) > len(s2):
            return False

        from collections import Counter
        count = Counter()

        for i in range(len(s1)):
            count[s1[i]] += 1
            count[s2[i]] -= 1
        if self.Iszero(count):
            return True

        for i in range(len(s1),len(s2)):
            count[s2[i]] -= 1
            count[s2[i - len(s1)]] += 1
            if self.Iszero(count):
                return True
        return False

    def Iszero(self, count):
        for i in count:
            if count[i] != 0:
                return False
        return True


        '''
        # same idea, but low complexity
        if len(s1) > len(s2):
            return False

        map1 = [0] * 26
        map2 = [0] * 26
        i = 0
        while i < len(s1):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1
            i += 1

        if map1 == map2:
            return True

        left = 0
        right = len(s1)
        while right < len(s2):
            map2[ord(s2[right]) - ord('a')] += 1
            map2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1

            if map1 == map2:
                return True

        return False
        '''
# test
s1 = "ab"
s2 = "eidboaoo"
Solution().checkInclusion(s1,s2)