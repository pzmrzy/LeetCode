class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(math.sqrt(area))
        for i in range(mid, -1, -1):
            if area % i == 0:
                return [area / i, i]
