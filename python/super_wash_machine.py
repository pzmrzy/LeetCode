class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        s = sum(machines)
        l = len(machines)
        average = s / l
        print average
        if average * l != s:
            return -1
        res = cnt = 0
        for load in machines:
            cnt += load - average
            res = max(res, abs(cnt), load - average);
        return res
