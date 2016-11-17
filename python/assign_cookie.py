class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        res = 0
        lg = len(g)
        ls = len(s)
        pg = 0
        ps = 0
        while pg < lg and ps < ls:
            if g[pg] <= s[ps]:
                res += 1
                pg += 1
                ps += 1
            else:
                ps += 1
        return res
