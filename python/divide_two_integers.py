class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxint = 2147483647
        sign = (dividend < 0) == (divisor < 0)
        if divisor == 0:
            return maxint
        if dividend == 0:
            return 0
        divisor, dividend = abs(divisor), abs(dividend)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                tmp <<= 1
                i <<= 1
        if not sign:
            res = -res
        return min(max(res, -maxint-1), maxint)
