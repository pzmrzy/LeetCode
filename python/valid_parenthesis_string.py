class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
                r += 1
            elif c == ')':
                l -= 1 if l > 0 else 0
                r -= 1
            else:
                l -= 1 if l > 0 else 0
                r += 1
            if r < 0:
                return False
        return l == 0
