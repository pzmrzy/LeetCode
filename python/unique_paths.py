class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        x = [1]*m
        for i in range(n-1):
            for j in range(m-1):
                x[j+1] = x[j+1] + x[j]
        return x[-1]
