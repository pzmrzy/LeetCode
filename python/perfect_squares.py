import math
class Solution(object):
    def chk(self, n):
        if math.sqrt(n) - int(math.sqrt(n)) < 0.00000001:
            return True
        else:
            return False
            
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.chk(n):
            return 1
        while n % 4 == 0:
            n /= 4
        if (n - 7) % 8 == 0:
            return 4
        for i in range(int(math.sqrt(n))):
            if self.chk(n-(i+1)*(i+1)):
                return 2
        return 3
