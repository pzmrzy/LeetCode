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
        new = [nums[0]]
        for n in nums[1:]:
            if n != new[-1]:
                new.append(n)
        n = len(new)
        return self.fmin(new, 0, n-1)
