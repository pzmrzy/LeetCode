class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        p = len(expression) - 1
        while p >= 0:
            if expression[p] == ':':
                p -= 1
            elif expression[p] == '?':
                e1 = stack.pop()
                e2 = stack.pop()
                if expression[p - 1] == 'T':
                    stack.append(e1)
                else:
                    stack.append(e2)
                p -= 2
            else:
                stack.append(expression[p])
                p -= 1
        return stack[0]
