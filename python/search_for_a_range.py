import sys
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [-sys.maxint] + nums + [sys.maxint]
        r = len(nums) - 1
        l = 0
        while True:
            mid1 = (l + r) / 2
            if nums[mid1] < target and nums[mid1 + 1] >= target:
                break
            if nums[mid1] == target:
                r = mid1 - 1
                continue
            if nums[mid1] < target:
                l = mid1+1
            else:
                r = mid1-1
        r = len(nums) - 1
        l = 0
        while True:
            mid2 = (l + r) / 2
            if nums[mid2] > target and nums[mid2 - 1] <= target:
                break
            if nums[mid2] == target:
                l = mid2 + 1
                continue
            if nums[mid2] < target:
                l = mid2+1
            else:
                r = mid2-1
        if mid2 - mid1 >= 2:
            return [mid1, mid2-2]
        else:
            return [-1, -1]
