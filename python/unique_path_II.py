class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
        for i in range(1,n):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] =0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
        
        return obstacleGrid[m-1][n-1]
