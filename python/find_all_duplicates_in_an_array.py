class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        res = []
        for i in range(l):
            ind = abs(nums[i]) - 1
            if nums[ind] < 0:
                res.append(ind + 1)
            else:
                nums[ind] *= -1
        return res
