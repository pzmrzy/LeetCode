class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = [0, 1]
        if n == 1:
            return res
        x = 1
        for i in range(n-1):
            x *= 2
            res = res+[x+i for i in reversed(res)]
        return res
