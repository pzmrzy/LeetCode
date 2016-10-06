import Queue
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = {}
        n = len(equations)
        for i in xrange(n):
            x, y = equations[i]
            v = values[i]
            dic.setdefault(x, [])
            dic.setdefault(y, [])
            dic[x].append((y, v))
            dic[y].append((x, 1.0 / v))
        res = []
        for q in queries:
            x, y = q
            if x not in dic or y not in dic:
                res.append(-1.0)
                continue
            if x == y:
                res.append(1.0)
                continue
            que = Queue.Queue()
            visit = {}
            visit[x] = True
            que.put((x,1))
            flag = False
            while not que.empty():
                now, dis = que.get()
                for v in dic[now]:
                    t, td = v
                    if t not in visit:
                        if t == y:
                            res.append(dis * td)
                            flag = True
                        else:    
                            que.put((t, dis * td))
                            visit[t] = True
                if flag:
                    break
            else:
                res.append(-1.0)
        return res
