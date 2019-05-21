class Solution:
    def findKthLargest(self, nums, k: int):
        '''
        :param nums: List[int]
        :param k: int
        :return: int
        '''
        # return sorted(nums,reverse=True)[k-1]
        left, right = 0, len(nums) - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            elif pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, nums, left, right):
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r
# test
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums,k))