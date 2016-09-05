class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        for x in range(int(math.pow(2, n))):
            a = [(x >> i) % 2 for i in range(n)]
            print a
            res.append([nums[i] for i in range(n) if a[i] == 1])
        return res
