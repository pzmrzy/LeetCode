import sys
class Solution(object):
    def check(self, now, req):
        for key in req:
            if now[key] < req[key]:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i = j = 0
        req = {}
        now = {}
        res = sys.maxint
        resstr = ""
        for c in t:
            req.setdefault(c, 0)
            req[c] += 1
            now[c] = 0
        for c in s:
            now[c] = 0
        for c in s:
            now[c] += 1

            if self.check(now, req):
                if j - i + 1 < res:
                    res = j - i + 1
                    resstr = s[i:j + 1]
                while True:
                    if s[i] in req:
                        now[s[i]] -= 1
                        if self.check(now, req):
                            i += 1
                            if j - i + 1 < res:
                                res = j - i + 1
                                resstr = s[i:j + 1]
                        else:
                            now[s[i]] += 1
                            if self.check(now, req):
                                if j - i + 1 < res:
                                    res = j - i + 1
                                    resstr = s[i:j + 1]
                            break
                    else:
                        i += 1
            j += 1
        return resstr
