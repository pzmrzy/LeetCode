class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0;
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if ((i > 0) and grid[i - 1][j] == 1):
                        res -= 1
                    if ((i < m - 1) and grid[i + 1][j] == 1):
                        res -= 1
                    if ((j > 0) and grid[i][j - 1] == 1):
                        res -= 1
                    if ((j < n - 1) and grid[i][j + 1] == 1):
                        res -= 1
        return res
