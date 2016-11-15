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
        flag = True
        for c in s:
            if c in "1234567890":
                tmp = tmp * 10 + int(c)
                flag = True
            elif c in "+-":
                if flag:
                    pool.append(tmp)
                tmp = 0
                while True:
                    if len(signstack) == 0 or signstack[-1] == "(":
                        signstack.append(c)
                        break
                    else:
                        pool.append(signstack.pop())

            elif c in "*/":
                if flag:
                    pool.append(tmp)
                tmp = 0
                while True:
                    if len(signstack) == 0 or signstack[-1] == "(":
                        signstack.append(c)
                        break
                    elif signstack[-1] in "*/":
                        pool.append(signstack.pop())
                    else:
                        signstack.append(c)
                        break
            elif c == "(":
                signstack.append('(')
            elif c == ")":
                if flag:
                    pool.append(tmp)
                tmp = 0
                flag = False
                while True:
                    if signstack[-1] != '(':
                        pool.append(signstack.pop())
                    else:
                        signstack.pop()
                        break
        if flag:
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
