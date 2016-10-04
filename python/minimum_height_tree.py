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


	if n == 1:
            return [0]
        dic = {}
        for e in edges:
            x, y = e
            dic.setdefault(x, [])
            dic.setdefault(y, [])
            dic[x].append(y)
            dic[y].append(x)
        depth = [0] * n
        q = Queue.Queue()
        q.put((0, 0))
        close = {}
        while not q.empty():
            node, dep = q.get()
            depth[node] = dep
            close[node] = True
            for v in dic[node]:
                if v not in close:
                    q.put((v, dep + 1))

        m = max(depth)
        ind = depth.index(m)

        depth = [0] * n
        q = Queue.Queue()
        q.put((ind, 0))
        close = {}
        father = {ind: None}
        while not q.empty():
            node, dep = q.get()
            depth[node] = dep
            close[node] = True
            for v in dic[node]:
                if v not in close:
                    q.put((v, dep + 1))
                    father[v] = node

        m = max(depth)
        ind1 = depth.index(m)

        if depth[ind1] % 2 == 1:
            ad = depth[ind1] / 2
            t = ind1
            for i in range(ad):
                t = father[t]
            return [t, father[t]]
        else:
            ad = depth[ind1] / 2
            t = ind1
            for i in range(ad):
                t = father[t]
            return [t]
