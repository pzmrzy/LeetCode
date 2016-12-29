class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dp(x, y):
            if data[x][y] == -1:
                val = matrix[x][y]
                data[x][y] = 1 + max(
                    dp(x - 1, y) if x > 0 and val > matrix[x - 1][y] else 0,
                    dp(x + 1, y) if x < m - 1 and val > matrix[x + 1][y] else 0,
                    dp(x, y - 1) if y > 0 and val > matrix[x][y - 1] else 0,
                    dp(x, y + 1) if y < n - 1 and val > matrix[x][y + 1] else 0)
            return data[x][y]
            
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        data = [[-1] * n for i in range(m)]
        return max(dp(x, y) for x in range(m) for y in range(n))
