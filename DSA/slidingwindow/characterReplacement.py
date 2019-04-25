class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        :param s: str
        :param k: int
        :return: int
        '''

        # idea: use sliding window, move end and obtain the freq of each letter.
        # get the max_cnt, if end-start+1-max_cnt > k, need to reduce count of start by 1,
        # and move start forward. update the max_len.
        # Time O(n), Space O(1).
        # only 26 letters, can use array; other case, can use Counter

        from collections import Counter
        count = Counter() # count = [0] * 26
        start, max_cnt, max_len = 0, 0, 0
        for end in range(len(s)):
            count[s[end]] += 1 # count[ord(s[end]) - ord('A')] += 1
            max_cnt = max(max_cnt, count[s[end]])
            while end - start + 1 - max_cnt > k: # need to reduce the sliding window
                count[s[start]] -= 1 # reduce the count of start letter
                start += 1 # move forward start
            max_len = max(max_len, end - start + 1)
        return max_len

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s,k))