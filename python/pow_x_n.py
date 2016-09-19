class Solution(object):
    def p(self, x, n):
        if (n == 0):
            return 1
        if (n == 1):
            return x
        t = self.p(x, n / 2)
        if n % 2 == 0:
            return t * t
        else:
            return t * t * x
            
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n > 0:
            return self.p(x, n)
        else:
            return 1 / self.p(x, -n)
