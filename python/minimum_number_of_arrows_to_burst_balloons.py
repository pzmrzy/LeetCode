import sys
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        l, r = sys.maxint, -sys.maxint
        for x, y in sorted(points):
            if l <= x <= r:
                l, r = max(l, x), min(r, y)
            else:
                l, r = x, y
                res += 1
        return res
