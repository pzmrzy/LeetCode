class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inbound = [0] * numCourses
        dic = {}
        for i in range(numCourses):
            dic.setdefault(i, [])
        for x, y in prerequisites:
            inbound[x] += 1
            dic[y].append(x)
        while True:
            try:
                t = inbound.index(0)
                for m in dic[t]:
                    inbound[m] -= 1
                inbound[t] = -1
            except:
                if sum([i for i in inbound if i > 0]) == 0:
                    return True
                else:
                    return False
