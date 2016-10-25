class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) + 1 != n:
            return False
        dic = {}
        for i in range(n):
            dic[i] = []
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        close = set([0])
        q = [0]
        while len(q) > 0:
            now = q[0]
            for v in dic[now]:
                if v not in close:
                    q.append(v)
                    close.add(v)
            del q[0]
        return len(close) == n
