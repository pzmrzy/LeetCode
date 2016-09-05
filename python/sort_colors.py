class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        m = 0
        while m <= r:
            if nums[m] == 1:
                m += 1
            elif nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
