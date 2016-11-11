# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import Queue

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        res = 0
        intervals = [(i.start, i.end) for i in intervals]
        intervals.sort()
        q = Queue.PriorityQueue()
        for s, e in intervals:
            if not q.empty():
                t = q.get()
                if t > s:
                    q.put(t)
            
            q.put(e)
            res = max(res, q.qsize())
        return res
