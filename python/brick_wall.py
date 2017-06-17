from collections import defaultdict
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(lambda: 0)
        for row in wall:
            tmp = 0
            for c in row[:-1]:
                tmp += c
                dic[tmp] += 1
        if len(dic) == 0:
            return len(wall)
        return len(wall) - max(dic.values())
