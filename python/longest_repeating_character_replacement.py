import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ln = len(s)
        count = collections.defaultdict(lambda :0)
        l = tmp = res = 0
        for r in range(ln):
            count[s[r]] += 1
            tmp = max(tmp, count[s[r]])
            while r - l + 1 - tmp > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
