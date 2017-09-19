class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = x / 2 + 1
        while res * res > x:
            res = (res + x / res) / 2
        return res

class Solution(object):
    def find(self, x, l, r):
        m = (l + r) / 2
        if (m * m <= x and (m+1) * (m+1) > x):
            return m
        if (m * m > x):
            return self.find(x, l, m)
        else:
            return self.find(x, m, r)
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        tmp = x / 2
        return self.find(x, 0, x)

