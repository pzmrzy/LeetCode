class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ts in s:
            dic.setdefault(ts, 0)
            dic[ts] += 1
        flag = 0
        res = 0
        for key in dic:
            if dic[key] % 2 == 0:
                res += dic[key]
            else:
                res += dic[key] - 1
                flag = 1
        return res + flag
