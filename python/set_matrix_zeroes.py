class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        fm = fn = 1
        for i in range(m):
            if matrix[i][0] == 0:
                fm = 0
                break
        for i in range(n):
            if matrix[0][i] == 0:
                fn = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0                    
                    
        if fm == 0:
            for i in range(m):
                matrix[i][0] = 0
        if fn == 0:
            for i in range(n):
                matrix[0][i] = 0
                    
