class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        if la < lb:
            a = '0'*(lb-la)+a
        else:
            b = '0'*(la-lb)+b
        a = a[::-1]
        b = b[::-1]
        c = 0
        n = len(a)
        res = [0 for i in range(n)]
        for i in range(n):
            t = c + int(a[i]) + int(b[i])
            res[i] = t % 2
            c = t / 2
        if c == 1:
            res.append(1)
        return "".join(map(str, res))[::-1]
