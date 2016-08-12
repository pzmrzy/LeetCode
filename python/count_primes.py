class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        p = [True for i in range(n)]
        p[0] = False
        p[1] = False
        for i in range(n):
            if p[i]:
                t = i*i
                while t < n:
                    p[t] = False
                    t += i
        res = 0
        for i in range(n):
            if p[i]:
                res += 1
        return res
