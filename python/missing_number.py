class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (0 + len(nums)+1) * len(nums) / 2 - sum(nums)
