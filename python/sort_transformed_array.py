class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = []
        for i in nums:
            n.append(a * i * i + b * i + c)
        res = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            fl, fr = n[l], n[r]
            if (a > 0) ^ (fl > fr):
                res.append(fr)
                r -= 1
            else:
                res.append(fl)
                l += 1
        return res[::-1] if a > 0 else res
