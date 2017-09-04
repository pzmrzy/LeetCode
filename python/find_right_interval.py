# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        data = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        l = len(intervals)
        for e in intervals:
            r = bisect.bisect_left(data, (e.end, ))
            res.append(data[r][1] if r < l else -1)
        return res
