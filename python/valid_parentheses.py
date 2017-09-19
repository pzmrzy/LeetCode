class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {']':'[', ')':'(', '}':'{'}
        left = set(['(', '[', '{'])
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != dic[c]:
                    return False
        return stack == []
