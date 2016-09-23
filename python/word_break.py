class Solution(object):
    def dp(self, i, j):
        if self.s[i:j] in self.dic:
            self.data[i][j] = True
            return True
        if i + 1 == j:
            self.data[i][j] = False
            return False
        for k in range(i+1, j):
            if self.data[i][k] == -1:
                self.dp(i, k)
            if self.data[k][j] == -1:
                self.dp(k, j)
            if self.data[i][k] and self.data[k][j]:
                self.data[i][j] = True
                return True
        self.data[i][j] = False
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False
        self.dic = {}
        self.s = s
        n = len(s)
        self.data = [[-1 for i in range(n + 1)] for j in range(n + 1)]
        for w in wordDict:
            self.dic.setdefault(w, True)
        return self.dp(0, n)
