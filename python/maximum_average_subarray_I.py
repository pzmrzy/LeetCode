class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        now = sum(nums[:k])
        res = now
        i, j = 0, k
        while j < len(nums):
            now = now - nums[i] + nums[j]
            if now > res:
                res = now
            i += 1
            j += 1
        return float(res) / k
