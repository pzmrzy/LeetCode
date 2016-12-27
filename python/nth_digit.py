class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, count, start = 1, 9, 1
        while n > l * count:
            n -= l * count
            l += 1
            count *= 10
            start *= 10
        start += (n - 1) / l
        return int(str(start)[(n - 1) % l])
