class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        res = 0
        status = 0
        for c in s:
            if c == ' ':
                if status == 1:
                    res += 1
                status = 0
            else:
                status = 1
        return res if s[-1] == ' ' else res + 1
