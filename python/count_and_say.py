class Solution(object):
    def read(self, s):
        cnt = 1
        now = s[0]
        ret = ""
        for c in s[1:]:
            if c == now:
                cnt += 1
            else:
                ret += "%s%s" % (cnt, now)
                now = c
                cnt = 1
        ret += "%s%s" % (cnt, now)
        return ret
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            s = self.read(s)
        return s
