class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            return gcd(b % a, a) if a != 0 else abs(b)
        
        ints = re.findall("[+-]?\d+", expression)
        A, B = 0, 1
        #A/B+a/b = A*b+a*B / Bb
        for i in range(len(ints) / 2):
            a, b = int(ints[2 * i]), int(ints[2 * i + 1])
            A = A * b + a * B
            B = B * b
        g = gcd(A, B)
        return "%s/%s" % (A / g, B / g)
