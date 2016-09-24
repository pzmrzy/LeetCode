class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0":
            return 0
        pat = ['00', '30', '40', '50', '60', '70', '80', '90']
        for p in pat:
            if s.find(p) != -1:
                return 0
        n = len(s)
        data = [-1 for _ in range(n+1)]
        data[0] = 1
        data[1] = 1
        for i in range(2,n+1):
            t = 0
            if s[i-1] != '0':
                t = data[i-1]
                if 10 <= int(s[i-2]) * 10 + int(s[i-1]) <= 26:
                    t += data[i-2]
            else:
                t = data[i-2]
            data[i] = t
        return data[n]
