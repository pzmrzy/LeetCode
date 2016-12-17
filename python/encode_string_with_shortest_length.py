class Solution:
    def __init__(self):
        self.dp = {}

    def solve(self, s):
        res = s
        l = len(s)
        for i in range(1, l / 2 + 1):
            if l % i or s[:i] * (l / i) != s:
                continue
            t = "%s[%s]" % (l / i, self.encode(s[:i]))
            if len(t) < len(res):
                res = t
        return res

    def encode(self, s):
        l = len(s)
        if l <= 1:
            return s
        if s in self.dp:
            return self.dp[s]
        res = s
        for i in range(1, l + 1):
            left, right = s[:i], s[i:]
            t = self.solve(left) + self.encode(right)
            if len(t) < l:
                res = t
        self.dp[s] = res
        return res
