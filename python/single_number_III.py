ass Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = reduce(lambda x, y: x ^ y, nums)
        x = x & ~(x - 1)
        res0 = res1 = 0
        for n in nums:
            if n & x == 0:
                res0 ^= n
            else:
                res1 ^= n
        return [res0, res1]
