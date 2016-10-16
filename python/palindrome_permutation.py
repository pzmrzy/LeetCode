class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            dic.setdefault(c, 0)
            dic[c] += 1
        tmp = 0
        for key in dic:
            if dic[key] % 2 == 1:
                tmp += 1
        if tmp > 1:
            return  False
        else:
            return True
