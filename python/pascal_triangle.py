class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1],[1,1]]
        for i in range(2, numRows):
            tmp = [0] + res[-1] + [0]
            now = []
            for j in range(len(tmp)-1):
                now.append(tmp[j]+tmp[j+1])
            res.append(now)
        return res
