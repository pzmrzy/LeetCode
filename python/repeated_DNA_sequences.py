class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        see = set()
        for i in range(len(s)-9):
            tmp = s[i: i+10]
            if tmp in see:
                res.add(tmp)
            see.add(tmp)
        return list(res)
