class Solution(object):
    def convert(self, s):
        if len(s) == 1:
            return tuple()
        ret = []
        for i in range(1, len(s)):
            t = ord(s[i]) - ord(s[i - 1])
            ret.append(t if t > 0 else t + 26)
        return tuple(ret)
                
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            t = self.convert(s)
            dic.setdefault(t, [])
            dic[t].append(s)
        res = []
        for key in dic:
            res.append(dic[key])
        return res
