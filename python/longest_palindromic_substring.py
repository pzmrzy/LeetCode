class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        i = st = maxl = 0
        while i < l:
            if l - i <= maxl / 2:
                break
            j = k = i
            while k < l - 1 and s[k + 1] == s[k]:
                k += 1
            i = k + 1
            while k < l - 1 and j > 0 and s[k + 1] == s[j - 1]:
                k += 1
                j -= 1
            tmp = k - j + 1
            if tmp > maxl:
                st = j
                maxl = tmp
        return s[st: st + maxl]
