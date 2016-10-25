class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            self.matrix = []
            return
        n = len(matrix[0])
        self.matrix = matrix
        self.m = m
        self.n = n
        self.data = [[0 for i in range(n + 1)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                self.data[i][j + 1] = self.data[i][j] + matrix[i][j]

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        t = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(col, self.n):
            self.data[row][i + 1] += t

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        data = self.data
        for i in range(row1, row2 + 1):
            res += data[i][col2 + 1] - data[i][col1]
        return res

        # Your NumMatrix object will be instantiated and called as such:
        # numMatrix = NumMatrix(matrix)
        # numMatrix.sumRegion(0, 1, 2, 3)
        # numMatrix.update(1, 1, 10)
        # numMatrix.sumRegion(1, 2, 3, 4)
