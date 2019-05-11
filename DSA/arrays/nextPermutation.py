class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        '''
        note: i, j counts from back to forward        
        1. find 1st decrease ind i
        2. find 1st element with index j that larger than nums[i]
        3. swap nums[i] and nums[j]
        4. sorted nums[i+1:]
        '''
        if not nums:
            return None

        i = len(nums) - 1
        # notice that, after while loop,
        # i denotes the element after the 1st decrease ind
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1

        # if the list is already reversed sorted
        # return the reversed version of it
        if i == 0:
            return nums.reverse()
            # nums.reverse()
            # return
        else:
            # find 1st element with index j that larger than nums[i]
            j = len(nums) - 1
            while j > i-1:
                if nums[j] > nums[i-1]:
                    break
                j -= 1

            # swap
            nums[i-1], nums[j] = nums[j], nums[i-1]

            # sorted
            return nums[:i] + sorted(nums[i:])
            # nums[i:] = sorted(nums[i:])
            # return

# test
nums = [3,2,1]
# nums = [1,2,7,4,3,1]
print(Solution().nextPermutation(nums))

