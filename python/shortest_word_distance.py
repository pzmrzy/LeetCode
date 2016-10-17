import sys
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l = -1
        r = -1
        res = sys.maxint
        for i in range(len(words)):
            if words[i] == word1:
                l = i
            if words[i] == word2:
                r = i
            if l != -1 and r != -1:
                res = min(abs(l - r), res)
        return res
