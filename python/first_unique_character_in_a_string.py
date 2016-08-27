class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            dic.setdefault(c, 0)
            dic[c] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
