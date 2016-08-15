class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [1 for i in range(length)]
        l = 1
        for i in range(length):
            res[i] *= l
            l *= nums[i]
        r = 1
        for i in range(length-1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res
