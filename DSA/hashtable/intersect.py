class Solution:
    def intersect(self, nums1, nums2):
        '''
        :param nums1: List[int]
        :param nums2: List[int]
        :return: List[int]
        '''
        from collections import Counter
        a, b = Counter(nums1), Counter(nums2)
        res = []
        for i in a:
            if i in b:
                tmp = min(a[i],b[i])
                while tmp:
                    res.append(i)
                    tmp -= 1
        return res

        # return [res.append(i) for i in b if i in a]

# test
a = [1,2,2,1]
b = [2,2]
print(Solution().intersect(a,b))