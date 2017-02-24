import string
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        if len(word) == 1:
            return True
        lower = set([c for c in string.lowercase])
        upper = set([c for c in string.uppercase])
        if word[0] in upper:
            if word[1] in upper:
                for c in word[2:]:
                    if c in lower:
                        return False
            else:
                for c in word[2:]:
                    if c in upper:
                        return False
        else:
            for c in word[1:]:
                if c in upper:
                    return False
        return True
