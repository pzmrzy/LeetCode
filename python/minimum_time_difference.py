class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = []
        for time in timePoints:
            times.append(map(int, time.split(':')))
        times.sort()
        times.append([times[0][0] + 24, times[0][1]])
        l = len(times)
        res = 10000
        print times
        for i in range(l-1, 0, -1):
            tmp = (times[i][0] - times[i - 1][0]) * 60 + times[i][1] - times[i - 1][1]
            if tmp < res:
                res = tmp
        return res
