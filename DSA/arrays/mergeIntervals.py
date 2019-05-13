class Solution(object):
    def merge(self, intervals):
        res = []
        for i in sorted(intervals, key=lambda i: i[0]):
            # compare tail of range res with start of range i
            if res and i[0] <= res[-1][-1]:
                # update the tail of range res
                # choose the max one
                res[-1][-1] = max(res[-1][-1], i[-1])
            # else has two meanings
            # one is that res is empty
            # the other is that i[0] > res[-1][-1]
            # in these two cases,just add i to the tail of res
            else:
                res.append(i)
        return res

    # wrong
    # def merge(self, intervals):
    #     """
    #     :type intervals: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     intervals = sorted(intervals, key=lambda i: i[0])
    #     if not intervals:
    #         return []
    #     if len(intervals) == 1:
    #         return intervals
    #     first = intervals[0]
    #
    #     for i in range(1, len(intervals)):
    #         if intervals[i][0] <= first[-1]:
    #             if first[-1] >= intervals[i][-1]:
    #                 res.append(first)
    #             else:
    #                 res.append([first[0],intervals[i][-1]])
    #             first = res[-1]
    #         else:
    #             if first not in res:
    #                 res.append(first)
    #                 res.append(intervals[i])
    #             else:
    #                 res.append(intervals[i])
    #             first = res[-1]
    #     return res

# test
nums = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(nums))