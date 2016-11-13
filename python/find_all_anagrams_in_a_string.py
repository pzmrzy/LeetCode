from collections import defaultdict
class Solution(object):
    def getdict(self, s):
        ret = defaultdict(lambda: 0)
        for c in s:
            ret[c] += 1
        return ret

    def check(self, d1, d2):
        for key in d1:
            if d1[key] != d2[key]:
                return False
        return True

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls = len(s)
        lp = len(p)
        if ls == 0 or lp == 0:
            return []
        dictp = self.getdict(p)
        dicts = self.getdict(s[:lp])
        res = []
        if self.check(dictp, dicts):
            res.append(0)
        i = 1
        while i < ls - lp + 1:
            if s[i + lp - 1] not in dictp:
                if i + lp + lp <= ls:
                    dicts = self.getdict(s[i + lp: i + lp + lp])
                    i += lp
                    if self.check(dictp, dicts):
                        res.append(i)
                    i += 1
                else:
                    break
            if i + lp - 1 >= ls:
                break
            dicts[s[i - 1]] -= 1
            dicts[s[i + lp - 1]] += 1
            if self.check(dictp, dicts):
                res.append(i)
            i += 1
        return res
