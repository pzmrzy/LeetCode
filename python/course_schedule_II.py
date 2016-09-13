class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inbound = [0] * numCourses
        dic = {}
        for i in range(numCourses):
            dic.setdefault(i, [])
        for x, y in prerequisites:
            inbound[x] += 1
            dic[y].append(x)
        res = []
        while True:
            try:
                t = inbound.index(0)
                res.append(t)
                for m in dic[t]:
                    inbound[m] -= 1
                inbound[t] = -1
            except:
                if sum([i for i in inbound if i > 0]) == 0:
                    return res
                else:
                    return []
