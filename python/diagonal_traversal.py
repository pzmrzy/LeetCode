class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return [e[2] for e in sorted([(i + j, (j, i)[(i ^ j) & 1], val) for i, row in enumerate(matrix) for j, val in enumerate(row)])]
