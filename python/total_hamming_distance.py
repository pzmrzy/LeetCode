class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l = len(nums)
        for i in range(32):
            tmp = 0
            for n in nums:
                tmp += (n >> i) & 1
            res += tmp * (l - tmp)
        return res
