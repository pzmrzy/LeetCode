# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        now = intervals[0].end
        res = 0
        for i in intervals[1:]:
            if i.start < now:
                now = min(i.end, now)
                res += 1
            else:
                now = i.end
        return res
