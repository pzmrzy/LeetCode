class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p.replace("*", '')) > len(s):
            return False
        ls = len(s)
        lp = len(p)
        data = [[False for i in range(lp + 1)] for j in range(ls + 1)]
        data[0][0] = True
        for j in range(0, lp):
            if p[j] == '*':
                data[0][j + 1] = data[0][j]
        for i in range(0, ls):
            for j in range(0, lp):
                if s[i] == p[j] or p[j] == '?':
                    data[i + 1][j + 1] = data[i][j]
                if p[j] == '*':
                    data[i + 1][j + 1] = data[i + 1][j] or data[i][j + 1]
        return data[ls][lp]
