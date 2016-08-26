class Solution(object):
    def isVowels(self, c):
        return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        res = ['']*len(s)
        
        l = 0
        r = len(s)-1
        while True:
            f = False
            while True:
                if l > len(s) - 1:
                    f = True
                    break
                if self.isVowels(s[l]):
                    break
                else:
                    res[l] = s[l]
                    l += 1
            while True:
                if r < 0:
                    f = True
                    break
                if self.isVowels(s[r]):
                    break
                else:
                    res[r] = s[r]
                    r -= 1
            if f:
                break
            res[l] = s[r]
            res[r] = s[l]
            l+=1
            r-=1
            if l > r:
                break
        return ''.join(res)
        
