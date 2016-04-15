class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        d = [0] * L
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        for i in range(2,L):
            d[i] = max(d[i - 1], (d[i - 2] + nums[i]))
        return d[L - 1]
