class Solution(object):
    def bfs(self, matrix, q):
        m = len(matrix)
        n = len(matrix[0])
        ret = set([])
        while len(q) > 0:
            i, j = q[0]
            del q[0]
            ret.add((i, j))
            height = matrix[i][j]
            if i > 0 and matrix[i - 1][j] >= height:
                if (i - 1, j) not in ret:
                    q.append((i - 1, j))
                    ret.add((i - 1, j))
            if j > 0 and matrix[i][j - 1] >= height:
                if (i, j - 1) not in ret:
                    q.append((i, j - 1))
                    ret.add((i, j - 1))
            if i < m - 1 and matrix[i + 1][j] >= height:
                if (i + 1, j) not in ret:
                    q.append((i + 1, j))
                    ret.add((i + 1, j))
            if j < n - 1 and matrix[i][j + 1] >= height:
                if (i, j + 1) not in ret:
                    q.append((i, j + 1))
                    ret.add((i, j + 1))
        return ret

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        q = []
        for i in range(m):
            q.append((i, 0))
        for i in range(n):
            q.append((0, i))
        pac = self.bfs(matrix, q)

        q = []
        for i in range(m):
            q.append((i, n - 1))
        for i in range(n):
            q.append((m - 1, i))
        atl = self.bfs(matrix, q)

        ans = pac.intersection(atl)
        return [list(x) for x in ans]
