class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        dic = {}
        inbound = {}
        for e in edges:
            x, y = e
            dic.setdefault(x, [])
            dic.setdefault(y, [])
            dic[x].append(y)
            dic[y].append(x)
            inbound.setdefault(x, 0)
            inbound.setdefault(y, 0)
            inbound[x] += 1
            inbound[y] += 1
        while True:
            if len(inbound) <= 2:
                break
            tmp = []
            for key in inbound:
                if inbound[key] == 1:
                    tmp.append(key)
            for t in tmp:
                for v in dic[t]:
                    if v in inbound:
                        inbound[v] -= 1
                del inbound[t]
        res = []
        for key in inbound:
            res.append(key)
        return res
