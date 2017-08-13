from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        l = len(s1)
        for i in range(1, l):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[l - i:]) and self.isScramble(s1[i:], s2[:l-i]):
                return True
        return False
