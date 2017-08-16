class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        l = len(s)
        for i in range(l):
            dic.setdefault(s[i],[])
            dic[s[i]].append(t[i])
        for key in dic:
            if len(set(dic[key])) >1:
                return False
        dic = {}
        l = len(t)
        for i in range(l):
            dic.setdefault(t[i],[])
            dic[t[i]].append(s[i])
        for key in dic:
            if len(set(dic[key])) >1:
                return False
        return True
