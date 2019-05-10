class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        from functools import reduce

        if digits == '':
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        return reduce(lambda acc, digit: [x + y for x in acc for y in mapping[digit]], digits, [''])

# test
digits = "23"
print(Solution().letterCombinations(digits))