class Solution:
    def plusOne(self, digits):
        '''
        :param digits: List[int]
        :return: List[int]
        '''
        # i = len(digits) - 1
        # while i >= 0:
        #     if digits[i] == 9:
        #         digits[i] = 0
        #     else:
        #         digits[i] += 1
        #         return digits
        #     i -= 1
        #
        # digits[0] = 1
        # digits.append(0)

        return list(map(int, str(int(''.join(map(str, digits))) + 1)))

# test
nums = [9,9,9]
print(Solution().plusOne(nums))
