class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])
        if n == 0:
            return matrix
        res = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    left = res[i - 1][j] + 1 if i > 0 else float('inf')
                    up = res[i][j - 1] + 1 if j > 0 else float('inf')
                    res[i][j] = min(res[i][j], up, left)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                right = res[i + 1][j] + 1 if i < m - 1 else float('inf')
                down = res[i][j + 1] + 1 if j < n - 1 else float('inf')
                res[i][j] = min(res[i][j], right, down)
        return res
