class Solution(object):
    def check(self, s):
        n = len(s)
        for i in range(n / 2):
            if s[i] != s[n - i - 1]:
                return False
        return True

    def dp(self, i, j):
        if i > j:
            return ""
        if self.check(self.s[i:j + 1]):
            self.data[i][j] = self.s[i:j + 1]
            return self.s[i:j + 1]
        if self.data[i + 1][j] == -1:
            self.dp(i + 1, j)
        if self.data[i][j - 1] == -1:
            self.dp(i, j - 1)
        tmp = 0
        if len(self.data[i + 1][j]) > tmp:
            tmp = len(self.data[i + 1][j])
            self.data[i][j] = self.data[i + 1][j]
        if len(self.data[i][j - 1]) > tmp:
            tmp = len(self.data[i][j - 1])
            self.data[i][j] = self.data[i][j - 1]
        return tmp

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s[0]
        self.data = [[-1 for _ in range(n)] for i in range(n)]
        for i in range(n):
            self.data[i][i] = s[i]
        for i in range(n - 1):
            self.data[i][i + 1] = s[i:i + 2] if s[i] == s[i + 1] else s[i:i+1]
        if self.data[0][n - 1] == -1:
            self.dp(0, n - 1)
        return self.data[0][n - 1]
