class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        nums.sort()
        l = len(nums)
        res = 0
        for i in range(l - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
