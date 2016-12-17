class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        l = len(s)
        for i in range(l):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        res = 0
        if len(stack) == 0:
            return l
        else:
            for i in range(1, len(stack)):
                res = max(stack[i] - stack[i - 1] - 1, res)
        return max(l - stack[-1] - 1, res, stack[0])
