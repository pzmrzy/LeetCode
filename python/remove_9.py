class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        base = 1
        while (n > 0):
            res += n % 9 * base
            n /= 9
            base *= 10
        return res
