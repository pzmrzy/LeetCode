from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        res = 0
        for x in c:
            if x + 1 in c:
                res = max(res, c[x] + c[x + 1])
        return res
