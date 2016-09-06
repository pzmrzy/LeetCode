class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            tmp = res[:]
            for t in tmp:
                res.append(t+[n])
        return res
