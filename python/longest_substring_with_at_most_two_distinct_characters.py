class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, left, right = 0, 0, -1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                continue
            if right >= 0 and s[i] != s[right]:
                res = max(res, i - left)
                left = right + 1
            right = i - 1
        return max(res, len(s) - left)
