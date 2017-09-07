class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            ct = 0
            for c in s:
                if c == '(':
                    ct += 1
                elif c == ')':
                    ct -= 1
                    if ct < 0:
                        return False
            return ct == 0
        q = {s}
        while True:
            valid = filter(isvalid, q)
            if valid:
                return valid
            q = {s[:i] + s[i + 1:] for s in q for i in range(len(s))}
