class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find(0, len(nums) - 1, nums)
        
    def find(self, l, r, nums):
        if (l == r):
            return l
        if (l + 1 == r):
            return l if nums[l] > nums[r] else r
        mid = (l + r) / 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid - 1] < nums[mid] < nums[mid + 1]:
            return self.find(mid + 1, r, nums)
        return self.find(l, mid - 1, nums)
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
