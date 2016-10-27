import sys
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxint
        n1 = -1
        n2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                n1 = i
                if n2 != -1:
                    t = abs(n1 - n2)
                    if 0 < t < res:
                        res = t
            if words[i] == word2:
                n2 = i
                if n1 != -1:
                    t = abs(n1 - n2)
                    if 0 < t < res:
                        res = t
        return res
