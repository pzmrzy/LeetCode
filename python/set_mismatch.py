class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = sum(nums)
        s = set()
        dup = 0
        for n in nums:
            if n in s:
                dup = n
                break
            s.add(n)
        l = len(nums)
        tmp = (1 + l) * l / 2 - sums
        return [dup, dup + tmp]
