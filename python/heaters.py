import sys
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [sys.maxint]
        i = res = 0
        for h in sorted(houses):
            while h >= (heaters[i] + heaters[i + 1]) / 2.:
                i += 1
            res = max(res, abs(heaters[i] - h))
        return res
