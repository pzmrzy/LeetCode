class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(s)
        lt = len(t)
        if ls > lt:
            s, t = t, s
            ls, lt = lt, ls
        if ls == lt:
            tmp = 0
            for i in range(ls):
                if s[i] != t[i]:
                    tmp += 1
            return tmp == 1
        elif ls + 1 == lt:
            for i in range(ls):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True
        else:
            return False
