class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) > len(nums) / 2:
                return i
        """
        dic = {}
        l = len(nums)
        l = l / 2
        for n in nums:
            dic.setdefault(n, 0)
            dic[n] += 1
        for key in dic:
            if dic[key] >= l:
                return key
        """
