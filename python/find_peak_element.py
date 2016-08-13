import sys
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        nums.append(-sys.maxint-1)
        for i in range(len(nums)-2):
            if (nums[i+1] > nums[i]) and (nums[i+1] > nums[i+2]):
                return i+1
