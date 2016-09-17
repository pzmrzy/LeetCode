class Solution(object):
    def fmin(self, nums, l, r):
        if l == r:
            return nums[l]
        if nums[l] < nums[r]:
            return nums[l]
        else:
            mid = (l + r) / 2
            return min(self.fmin(nums, l, mid), self.fmin(nums, mid + 1, r))
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.fmin(nums, 0, n-1)
