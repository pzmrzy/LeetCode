class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = []
        l = len(points)
        for k in range(l):
            now = points[k]
            dic = {}

            for t in range(l):
                if k == t:
                    continue
                p = points[t]
                dist = abs(now[0] - p[0]) ** 2 + abs(now[1] - p[1]) ** 2
                dic.setdefault(dist, [])
                dic[dist].append(p)
            can = dic.values()
            lc = len(can)
            for sd in can:
                if len(sd) < 2:
                    continue
                for i in range(len(sd)):
                    for j in range(len(sd)):
                        if i != j:
                            res.append([now, sd[i], sd[j]])
        return len(res)
