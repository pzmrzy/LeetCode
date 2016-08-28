class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(n-1):
            grid[0][i+1] += grid[0][i]
        for i in range(m-1):
            grid[i+1][0] += grid[i][0]
            for j in range(n-1):
                grid[i+1][j+1] += min(grid[i][j+1], grid[i+1][j])

        return grid[m-1][n-1]
