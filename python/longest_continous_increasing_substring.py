class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        if n == 0:
            return 0
        now = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                now += 1
            else:
                res = max(res, now)
                now = 1
        return max(res, now)
