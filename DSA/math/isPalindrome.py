class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if len(x) % 2 == 0:
            if x[:len(x)//2] == x[len(x)//2:][::-1]:
                return True
            else:
                return False
        else:
            if x[:len(x) // 2] == x[len(x) // 2 + 1:][::-1]:
                return True
            else:
                return False


# test
x = 11
print(Solution().isPalindrome(x))