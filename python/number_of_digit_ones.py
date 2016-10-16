class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, m = 0, 1
        while m <= n:
            res += (n / m + 8) / 10 * m + (n / m % 10 == 1) * (n % m + 1)
            m *= 10
        return res
