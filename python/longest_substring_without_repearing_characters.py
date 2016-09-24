class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = j = 0
        res = 0
        dic = {}
        while i < n and j < n:
            if s[j] in dic:
                del dic[s[i]]
                i += 1
            else:
                dic[s[j]] = True
                j += 1
                res = max(res, j - i)
        return res
