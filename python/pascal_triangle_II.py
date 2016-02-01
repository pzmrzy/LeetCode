class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        result = [0 for i in range(rowIndex)]
        result[0] = 1
        for i in range(rowIndex):
            for j in range(i):
                if (i - j) == 0:
                    continue
                result[i - j] += result[i - j - 1]
        return result
