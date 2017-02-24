class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = 0
        res = 0
        dic = {0:0}
        for i, n in enumerate(nums, 1):
            ct += -1 if n == 0 else 1
            if ct in dic:
                res = max(res, i - dic[ct])
            else:
                dic[ct] = i
        return res
