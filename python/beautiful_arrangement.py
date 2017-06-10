class Solution(object):
    def dfs(self, num, now):
        if now == 0:
            self.res += 1
            return
        for i in range(now, 0, -1):
            num[i], num[now] = num[now], num[i]
            if num[now] % now == 0 or now % num[now] == 0:
                self.dfs(num, now - 1)
            num[now], num[i] = num[i], num[now]
        
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = [i for i in range(N + 1)]
        self.res = 0
        self.dfs(num, N)
        return self.res
