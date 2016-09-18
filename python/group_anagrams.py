class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            t = "".join(sorted(s))
            dic.setdefault(t, [])
            dic[t].append(s)
        res = []
        for key in dic:
            t = []
            for s in dic[key]:
                t.append(s)
            res.append(t)
        return res
