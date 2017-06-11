class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minx = m
        miny = n
        for x, y in ops:
            minx = min(minx, x)
            miny = min(miny, y)
        return minx * miny
