class Solution(object):
    def dp(self, s, i, j, data):
        if data[i][j] != -1:
            return data[i][j]
        if (i > j):
            return 0
        if (i == j):
            return 1
        if (s[i] == s[j]):
            data[i][j] = self.dp(s, i + 1, j - 1, data) + 2
        else:
            data[i][j] = max(self.dp(s, i + 1, j, data), self.dp(s, i, j - 1, data))
        return data[i][j]
        
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        data = [[-1] * l for i in range(l)]
        return self.dp(s, 0, l - 1, data)
