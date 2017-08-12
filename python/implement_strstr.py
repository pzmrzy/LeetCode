class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if haystack[i: i + l] == needle:
                return i
        return -1
