class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        res = [0] * (n + 1)
        res[0] = res[1] = 1
        for i in range(2, n + 1):
            tmp = 0
            for j in range(0, i):
                tmp += res[j] * res[i - 1 - j]
            res [i] = tmp
        return res[n]
