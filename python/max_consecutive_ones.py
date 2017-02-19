class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        ct = 0
        for i in nums:
            if i == 1:
                ct += 1
                res = max(res, ct)
            else:
                ct = 0
        return res
