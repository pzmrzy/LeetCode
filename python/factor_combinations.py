class Solution(object):
    def dfs(self, n, res, now, start):
        if now:
            res.append(now + [n])
        
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                self.dfs(n / i, res, now + [i], i)
        return res
        
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.dfs(n, [], [], 2)
