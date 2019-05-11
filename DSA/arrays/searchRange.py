class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        midind = self.checkind(nums, target)

        if midind == -1:
            return [-1, -1]

        i, j = midind,midind
        while i >= 0:
            if nums[i] != target:
                break
            i -= 1
        while j <= len(nums) - 1:
            if nums[j] != target:
                break
            j += 1
        return [i+1, j-1]

    def checkind(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1




# test
# nums = [5,6,6,6,7,7,7,8,8,8,10]
nums = [5,7,7,8,8,10]
tar= 6
print(Solution().searchRange(nums, tar))