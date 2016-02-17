class Solution(object):
    def find(self, matrix, l, r, X, Y, t):
        if (l > r):
            return False
        
        m = (l + r) / 2
        x = m / Y
        y = m % Y
        f = matrix[x][y]
        
        if (f == t):
            return True
        if (l == r):
            return False
        if (f > t):
            return self.find(matrix, l, max(m - 1, 0), X, Y, t)
        else:
            return self.find(matrix, m + 1, r, X, Y, t)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        X = len(matrix)
        Y = len(matrix[0])
        if (X == 0 or Y == 0):
            return False
        return self.find(matrix, 0, X*Y-1, X, Y, target)

