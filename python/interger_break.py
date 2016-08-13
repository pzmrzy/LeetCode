import math
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n== 4:
            return 4
        if n % 3 == 0:
            return int(math.pow(3, n / 3))
        if n % 3 == 1:
            return int(math.pow(3, n / 3 - 1)) * 4
        if n % 3 == 2:
            return int(math.pow(3, n / 3)) * 2
