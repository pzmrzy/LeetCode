class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        l = len(str)
        t = ""
        for i in range(0, l / 2):
            t += str[i]
            if l % (i + 1) == 0:
                if t * (l / (i + 1)) == str:
                    return True
        return False
