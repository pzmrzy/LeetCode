class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0:
            return True
        sp = set([])
        for x, y in points:
            sp.add((x, y))
        points = list(sp)
        points.sort()
        n = len(points)
        if n % 2 == 0:
            Y = float(points[0][0] + points[-1][0]) / 2
        else:
            Y = points[n / 2][0]
        s = set([])
        for x, y in points:
            s.add( (x, y) )
        for i in range(n):
            x, y = points[i]
            t = 2 * Y - x
            if (t, y) not in s:
                return False
        return True
