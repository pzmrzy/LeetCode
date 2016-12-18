class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            ind = abs(nums[i]) - 1
            nums[ind] = -abs(nums[ind])
        res = []
        for i in range(l):
            if (nums[i] > 0):
                res.append(i + 1)
        return res
