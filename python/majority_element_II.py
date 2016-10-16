class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        res = []
        for n in set(nums):
            if nums.count(n) > len(nums) / 3:
                res.append(n)
        return res
