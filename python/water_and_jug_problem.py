class Solution(object):
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            temp = a % b
            a = b
            b = temp
        return a

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if z > x + y:
            return False
        return z % self.gcd(x, y) == 0
