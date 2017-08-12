class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for i in xrange(upper, lower - 1, -1):
            cand = int(str(i) + str(i)[::-1])
            for j in xrange(upper, int(math.sqrt(cand)) - 1, -1):
                if cand % j == 0 and cand / j <= upper:
                    return cand % 1337
        return -1
