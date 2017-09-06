class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                x = stack.pop()
                y = stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(c))
        return stack.pop()
