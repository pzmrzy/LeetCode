class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        t = n / 2
        k = n - 1
        for i in range(t):
            for j in range(t):
                matrix[j][k-i], matrix[k-i][k-j], matrix[k-j][i], matrix[i][j] = matrix[i][j], matrix[j][k-i], matrix[k-i][k-j], matrix[k-j][i]
        if n % 2 == 1:
            i = (n - 1) / 2
            for j in range(t):
                matrix[j][k-i], matrix[k-i][k-j], matrix[k-j][i], matrix[i][j] = matrix[i][j], matrix[j][k-i], matrix[k-i][k-j], matrix[k-j][i]
