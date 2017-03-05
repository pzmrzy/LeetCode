class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m = len(picture)
        if m == 0:
            return 0
        n = len(picture[0])
        row = [0] * n
        col = [0] * m
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    col[i] += 1
                    row[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if col[i] == 1 and row[j] == 1:
                        res += 1
        return res
