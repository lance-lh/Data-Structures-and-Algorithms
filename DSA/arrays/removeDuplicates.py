class Solution:
    def removeDuplicates(self, nums):
        '''
        :param nums: list[int]
        :return: int
        '''
        if not nums:
            return 0

        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# test
nums = [1,1,2]
print(Solution().removeDuplicates(nums))