class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s.lower()
        s = re.sub(r'[^0-9a-z]', '', ss)
        l = len(s)
        result = True
        for i in range(l/2):
            if (s[i] != s[l - 1 - i]):
                result = False
                break
        return result
