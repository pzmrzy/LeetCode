ass Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        r, g, b = 0, 0, 0
        for i in range(n):
            lr, lg, lb = r, g, b
            r = min(lg, lb) + costs[i][0]
            g = min(lr, lb) + costs[i][1]
            b = min(lr, lg) + costs[i][2]
        return min(r, g, b)
