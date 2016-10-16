class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        l = len(s)
        for i in range(1, l):
            if s[i] == s[i - 1] == '+':
                res.append(s[:i - 1] + '--' + s[i + 1:])
        return res
