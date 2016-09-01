class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def compre(s, t):
            if len(s) > len(t):
                tmp = s
                s = t
                t = tmp
            if s == t[:len(s)]:
                return s
            for i in range(len(s)+1):
                if s[:i] != t[:i]:
                    return s[:i-1]
                    
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        res = compre(strs[0], strs[1])
        for i in range(len(strs)-2):
            res = compre(res, strs[i+2])
        return res
