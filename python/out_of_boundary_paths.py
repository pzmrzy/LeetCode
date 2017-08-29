class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        data = [[0] * n for _ in range(m)]
        data[i][j] = 1
        res = 0
        for i in range(N):
            cur = data
            data = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for x, y in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                        if 0 <= x < m and 0 <= y < n:
                            data[x][y] += val
                        else:
                            res += val
        return res % (10 ** 9 + 7)
