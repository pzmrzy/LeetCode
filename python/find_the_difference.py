import string
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic1 = {}
        dic2 = {}
        for c in string.lowercase:
            dic1[c] = 0
            dic2[c] = 0
        for c in s:
            dic1[c] += 1
        for c in t:
            dic2[c] += 1
        for c in string.lowercase:
            if dic1[c] != dic2[c]:
                return c
