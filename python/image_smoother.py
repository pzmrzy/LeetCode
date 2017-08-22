import math
class Solution(object):
    def neighbour(self, i, j, m, n, M):
        ret = [M[i][j]]
        if i > 0:
            ret.append(M[i - 1][j])
        if i < m:
            ret.append(M[i + 1][j])
        if j > 0:
            ret.append(M[i][j - 1])
        if j < n:
            ret.append(M[i][j + 1])
        if i > 0 and j > 0:
            ret.append(M[i - 1][j - 1])
        if i > 0 and j < n:
            ret.append(M[i - 1][j + 1])
        if i < m and j > 0:
            ret.append(M[i + 1][j - 1])
        if i < m and j < n:
            ret.append(M[i + 1][j + 1])
        return ret


    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        if m == 0:
            return M
        n = len(M[0])
        if n == 0:
            return M
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp = self.neighbour(i, j, m - 1, n - 1, M)
                res[i][j] = int(math.floor(float(sum(tmp)) / len(tmp)))
        return res
