class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        l = len(timeSeries)
        if l == 0:
            return 0
        if l == 1:
            return duration
        res = duration
        for i in range(1, l):
            res += min(timeSeries[i] - timeSeries[i - 1], duration)
        return res
