class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dp(i, j):
            if i == j:
                data[i][j] = 1
                return 1
            if i > j:
                data[i][j] = 0
                return 0
            if data[i][j] != -1:
                return data[i][j]
            if data[i + 1][j] == -1:
                dp(i+1, j)
            ret = data[i + 1][j] + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    if data[i][k - 1] == -1:
                        dp(i, k - 1)
                    if data[k + 1][j] == -1:
                        dp(k + 1, j)
                    ret = min(ret, data[i][k - 1] + data[k + 1][j])
            data[i][j] = ret
            return ret
        l = len(s)
        data = [[-1] * (l + 1) for _ in range(l + 1)]
        return dp(0, len(s) - 1)
