class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == "":
            return 0
        tmp = s.strip().split(' ')
        result = len(tmp[-1])
        return result
