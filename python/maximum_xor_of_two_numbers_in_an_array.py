class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32, -1, -1):
            res <<= 1
            pre = {n >> i for n in nums}
            res += any(res ^ 1 ^ p in pre for p in pre)
        return res
