class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[0][0] = True
        for i in range(lp):
            dp[0][i + 1] = p[i] == '*' and dp[0][i - 1]
        for i in range(ls):
            for j in range(lp):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[ls][lp]
                    
