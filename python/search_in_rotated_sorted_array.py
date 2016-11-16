class Solution(object):
    def find(self, l, r, target, nums):
        if l > r:
            return -1
        mid = (l + r) / 2
        if target == nums[mid]:
            return mid
        if nums[mid] < nums[r]:
            if nums[mid] < target <= nums[r]:
                return self.find(mid + 1, r, target, nums)
            else:
                return self.find(l, mid - 1, target, nums)
        else:
            if nums[l] <= target < nums[mid]:
                return self.find(l, mid - 1, target, nums)
            else:
                return self.find(mid + 1, r, target, nums)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        return self.find(l, r, target, nums)
