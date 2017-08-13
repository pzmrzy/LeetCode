# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for obj in sorted(intervals, key = lambda x: x.start):
            if res and obj.start <= res[-1].end:
                res[-1].end = max(obj.end, res[-1].end)
            else:
                res.append(obj)
        return res
