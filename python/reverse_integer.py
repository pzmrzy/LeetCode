class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if (x < 0):
            x = -1 * x
            flag = -1
        result = 0
        while (x > 0):
            result *= 10
            result += x % 10
            x /= 10
        if (result > math.pow(2,31)):
            result = 0
        return flag * result
