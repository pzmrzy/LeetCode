class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        return 0 if l == 0 else sum(nums) - l * min(nums) 
