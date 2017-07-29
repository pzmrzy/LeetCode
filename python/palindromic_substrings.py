class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = len(s)
        for mid in range(l * 2 - 1):
            left = mid / 2
            right = left + mid % 2
            while left >= 0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
