class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        l = len(nums)
        if l < 3:
            return max(nums)
        for i in range(3):
            for j in range(i+1, l):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums[2]
