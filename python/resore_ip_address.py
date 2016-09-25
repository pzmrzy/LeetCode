class Solution(object):
    def ip(self, ind, dot, path):
        if dot == self.n - ind:
            return
        if dot == 0:
            if 0 < (self.n - ind) <= 3:
                tn = self.s[ind:]
                if int(tn) < 256 and (len(tn) == 1 or tn[0] != '0'):
                    self.res.append(path+[self.s[ind:]])
                    return
        for i in range(1, 4):
            try:
                tn = self.s[ind:ind+i]
                if int(tn) < 256 and (len(tn) == 1 or tn[0] != '0'):
                    self.ip(ind+i, dot-1, path+[self.s[ind:ind+i]])
            except:
                continue
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.n = len(s)
        if not (4 <= self.n <= 12):
            return []
        self.s = s
        self.res = []
        self.ip(0, 3, [])
        return [".".join(s) for s in self.res]

