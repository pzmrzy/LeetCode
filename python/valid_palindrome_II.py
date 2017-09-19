class Solution(object):
    def check(self, s, l, r, flag):
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if flag:
                    return self.check(s, l + 1, r, False) or self.check(s, l, r - 1, False)
                else:
                    return False
        return True
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.check(s, 0, len(s) - 1, True)
