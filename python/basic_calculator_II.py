class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        signstack = []
        pool = []
        tmp = 0
        s.replace(" ", "")
        for c in s:
            if c in "1234567890":
                tmp = tmp * 10 + int(c)
            elif c in "+-":
                pool.append(tmp)
                tmp = 0
                while True:
                    if len(signstack) == 0:
                        signstack.append(c)
                        break
                    else:
                        pool.append(signstack.pop())

            elif c in "*/":
                pool.append(tmp)
                tmp = 0
                while True:
                    if len(signstack) == 0:
                        signstack.append(c)
                        break
                    elif signstack[-1] in "*/":
                        pool.append(signstack.pop())
                    else:
                        signstack.append(c)
                        break
        pool.append(tmp)
        pool += signstack[::-1]
        cal = []
        for it in pool:
            if isinstance(it, int):
                cal.append(it)
            else:
                op2 = cal.pop()
                op1 = cal.pop()
                if it == '+':
                    cal.append(op1 + op2)
                elif it == '-':
                    cal.append(op1 - op2)
                elif it == '*':
                    cal.append(op1 * op2)
                else:
                    cal.append(op1 / op2)
        return cal[0]
