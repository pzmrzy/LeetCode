class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        if t == "":
            return False
        ls = len(s)
        lt = len(t)
        hs = 0
        ht = 0
        while True:
            if s[hs] == t[ht]:
                hs += 1
                ht += 1
            else:
                ht += 1
            if hs == ls:
                return True
            if ht == lt:
                return False
