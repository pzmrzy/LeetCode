class Solution(object):
    def solve(self, nums):
        def mul(n):
            return reduce(lambda x, y: x * y, n, 1)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        firstneg, lastneg, numneg = -1, -1, 0
        for i, n in enumerate(nums):
            if n < 0 :
                if firstneg == -1:
                    firstneg = i
                lastneg = i
                numneg += 1
        if numneg % 2 == 0:
            return mul(nums)
        if firstneg == lastneg:
            return max(mul(nums[:firstneg]), mul(nums[firstneg + 1:]))
        return max(mul(nums[:firstneg]), mul(nums[lastneg + 1:]),
                  mul(nums[firstneg + 1:]), mul(nums[:lastneg]))
    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        pre = 0
        for i, n in enumerate(nums):
            if n == 0:
                res = max(res, self.solve(nums[pre: i]))
                pre = i + 1
        res = max(res, self.solve(nums[pre:]))
        return res if pre == 0 else max(res, 0)
