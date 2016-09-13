class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 1:
            if n==3:
                res += 2
                break
            elif n % 4 == 1:
                n -= 1
            elif n % 4 == 3:
                n += 1
            else:
                n /= 2
            res += 1
        return res
