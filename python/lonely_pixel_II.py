class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
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
        dic = {}
        for i in range(m):
            key = tuple(picture[i])
            dic.setdefault(key, [0, []])
            dic[key][0] += 1
            for j in range(n):
                if picture[i][j] == 'B':
                    dic[key][1].append((i, j))
        res = 0
        for key in dic:
            if dic[key][0] != N:
                continue
            for x, y in dic[key][1]:
                if col[x] == N and row[y] == N:
                        res += 1
        return res
