class Solution:
    def myAtoi(self, s: str) -> int:
        """
        :type str: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        lst = list(s.strip())

        if len(lst) == 0:
            return 0

        sign = -1 if lst[0] == '-' else 1

        if lst[0] in ['-','+']:
            del lst[0]

        res = 0
        i = 0
        while i < len(lst) and lst[i].isdigit():
            res = res * 10 + ord(lst[i]) - ord('0')
            i += 1
        # if sign == -1, return sign * res
        # if sign == 1, return sign * res
        return max(-2**31,min(sign * res, 2**31-1))

# test
# sin = "   -42"
sin = " "
print(Solution().myAtoi(sin))