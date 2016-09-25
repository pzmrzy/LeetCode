class Solution(object):
    def com(self, l, n, d, k):
        if d == k:
            return [[l]]
        res = []
        for i in range(l+1, n + 1 - (k - d - 1)):
            tmp = self.com(i, n, d + 1, k)
            if l == 0:
                res += tmp
            else:
                for p in tmp:
                    res.append([l] + p)
        return res
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.com(0, n, 0, k)
